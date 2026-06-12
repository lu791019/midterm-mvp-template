#!/usr/bin/env python3
"""Run end-to-end checks for all midterm topic solution notebooks and APIs.

The solution notebooks use topic-local relative paths such as ``orders.csv``.
To test them without moving CSV files or mutating the working tree, this script
copies the repository to a temporary directory, copies each solution notebook
into its matching ``data/raw/topic_N`` directory, executes it there, then starts
FastAPI and probes the common endpoints.
"""

from __future__ import annotations

import json
import csv
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path


TOPICS = {
    1: {
        "tables": ["raw_orders", "cleaned_orders", "analyzed_orders"],
        "extra_endpoints": ["/stats/products", "/stats/countries"],
        "csv_files": ["orders.csv"],
        "required_columns": ["description", "quantity", "invoice_date", "unit_price", "country"],
        "analyzed_columns": ["category", "llm_insight"],
    },
    2: {
        "tables": ["raw_products", "cleaned_products", "analyzed_products"],
        "csv_files": ["products.csv"],
        "required_columns": ["title", "amazon_price", "flipkart_price"],
        "analyzed_columns": ["category", "llm_insight"],
    },
    3: {
        "tables": ["raw_tracks", "cleaned_tracks", "analyzed_tracks"],
        "csv_files": ["tracks.csv"],
        "required_columns": ["Track", "Artist", "Spotify Streams", "Release Date"],
        "analyzed_columns": ["genre_guess", "llm_insight"],
    },
    4: {
        "tables": ["raw_trips", "cleaned_trips", "analyzed_trips"],
        "csv_files": ["trips.csv", "taxi_zone_lookup.csv"],
        "required_columns": ["tpep_pickup_datetime", "PULocationID", "total_amount", "LocationID", "Zone"],
        "analyzed_columns": ["area_type", "llm_insight"],
    },
    5: {
        "tables": ["raw_jobs", "cleaned_jobs", "analyzed_jobs"],
        "csv_files": ["jobs.csv"],
        "required_columns": ["job_title", "salary_in_usd", "job_category"],
        "analyzed_columns": ["field", "llm_insight"],
    },
    6: {
        "tables": ["raw_realestate", "cleaned_realestate", "analyzed_realestate"],
        "csv_files": ["real_estate.csv"],
        "required_columns": ["縣市", "鄉鎮市區", "總價元", "建物型態"],
        "analyzed_columns": ["area_character", "llm_insight"],
    },
}

COMMON_ENDPOINTS = ["/health", "/summary", "/analyzed", "/report", "/stats"]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_repo(src: Path, dst: Path) -> None:
    def ignore(_dir: str, names: list[str]) -> set[str]:
        ignored = {".git", ".venv", "__pycache__", ".DS_Store"}
        return {name for name in names if name in ignored or name.endswith(".pyc")}

    shutil.copytree(src, dst, ignore=ignore)


def run(cmd: list[str], cwd: Path, log_path: Path) -> None:
    with log_path.open("w") as log:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=log,
            stderr=subprocess.STDOUT,
            text=True,
        )
    if result.returncode != 0:
        tail = "\n".join(log_path.read_text(errors="replace").splitlines()[-60:])
        raise RuntimeError(f"Command failed in {cwd}: {' '.join(cmd)}\n{tail}")


def notebook_text(path: Path) -> str:
    data = json.loads(path.read_text())
    return "\n".join("".join(cell.get("source", [])) for cell in data["cells"])


def validate_starter_notebook(work_repo: Path, topic: int) -> None:
    topic_dir = work_repo / "data" / "raw" / f"topic_{topic}"
    config = TOPICS[topic]
    starter = topic_dir / "pipeline_starter.ipynb"
    spec = topic_dir / "requirements_spec.md"

    if not starter.exists():
        raise RuntimeError(f"topic_{topic} missing pipeline_starter.ipynb")
    if not spec.exists():
        raise RuntimeError(f"topic_{topic} missing requirements_spec.md")

    raw_columns: set[str] = set()
    for csv_name in config["csv_files"]:
        csv_path = topic_dir / csv_name
        if not csv_path.exists():
            raise RuntimeError(f"topic_{topic} missing {csv_name}")
        with csv_path.open(newline="", encoding="utf-8-sig") as f:
            header = next(csv.reader(f))
        raw_columns.update(column.strip() for column in header)

    missing = [column for column in config["required_columns"] if column not in raw_columns]
    if missing:
        raise RuntimeError(f"topic_{topic} CSV columns missing from source data: {missing}")

    text = notebook_text(starter)
    if "product_name" in text:
        raise RuntimeError(f"topic_{topic} starter still references stale product_name")
    if "{chr(10).join" in text:
        raise RuntimeError(f"topic_{topic} starter contains unevaluated report expression")
    if 'output/report.md' in text:
        raise RuntimeError(f"topic_{topic} starter should write output/pipeline_doc.md, not output/report.md")
    if topic == 1 and '@api.get("/stats")' not in text and "TODO: /stats " not in text:
        raise RuntimeError("topic_1 starter does not expose or request the common /stats endpoint")
    if topic == 3 and "spotify_streams" in text:
        raise RuntimeError('topic_3 starter should reference "Spotify Streams", not spotify_streams')


def execute_notebook(work_repo: Path, topic: int, logs_dir: Path) -> None:
    topic_dir = work_repo / "data" / "raw" / f"topic_{topic}"
    solution = work_repo / "_instructor" / "solutions" / f"topic_{topic}_solution.ipynb"
    local_notebook = topic_dir / "solution_run.ipynb"
    shutil.copy2(solution, local_notebook)

    output = logs_dir / f"topic_{topic}_executed.ipynb"
    run(
        [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "solution_run.ipynb",
            "--output",
            str(output),
            "--ExecutePreprocessor.timeout=180",
        ],
        cwd=topic_dir,
        log_path=logs_dir / f"topic_{topic}_notebook.log",
    )


def code_cells(notebook: dict) -> list[dict]:
    return [cell for cell in notebook["cells"] if cell.get("cell_type") == "code"]


def set_cell_source(cell: dict, source: str) -> None:
    cell["source"] = [line + "\n" for line in source.strip("\n").splitlines()]
    cell["outputs"] = []
    cell["execution_count"] = None


def solution_code_sources(work_repo: Path, topic: int) -> list[str]:
    solution = work_repo / "_instructor" / "solutions" / f"topic_{topic}_solution.ipynb"
    data = json.loads(solution.read_text())
    return ["".join(cell.get("source", [])) for cell in code_cells(data)]


def direct_api_demo_code(topic: int) -> str:
    configs = {
        1: (
            "零售銷售分析 API",
            "cleaned_orders",
            "description, COUNT(*) as orders, ROUND(SUM(total_amount),2) as revenue",
            "description",
            "analyzed_orders",
            "description, category, llm_insight",
        ),
        2: (
            "B2C 電商競品比價 API",
            "cleaned_products",
            "title, amazon_price, flipkart_price, ROUND(price_diff,2) as diff",
            None,
            "analyzed_products",
            "title, category, llm_insight",
        ),
        3: (
            "音樂串流趨勢分析 API",
            "cleaned_tracks",
            'Track, Artist, "Spotify Streams" as streams',
            None,
            "analyzed_tracks",
            "Track, Artist, genre_guess, llm_insight",
        ),
        4: (
            "叫車服務交通熱點 API",
            "cleaned_trips",
            "pickup_borough, pickup_zone, COUNT(*) as trips, ROUND(AVG(total_amount),2) as avg_fare",
            "pickup_borough, pickup_zone",
            "analyzed_trips",
            "pickup_zone, area_type, llm_insight",
        ),
        5: (
            "求職媒合薪資洞察 API",
            "cleaned_jobs",
            "job_category, COUNT(*) as jobs, ROUND(AVG(salary_in_usd),0) as avg_salary",
            "job_category",
            "analyzed_jobs",
            "job_title, field, llm_insight",
        ),
        6: (
            "不動產房價趨勢 API",
            "cleaned_realestate",
            "縣市, COUNT(*) as 交易量, ROUND(AVG(總價萬),1) as 均價萬",
            "縣市",
            "analyzed_realestate",
            "鄉鎮市區, area_character, llm_insight",
        ),
    }
    title, stats_table, stats_select, group_by, analyzed_table, analyzed_select = configs[topic]
    if topic == 1:
        stats_sql = (
            f"SELECT {stats_select} FROM {stats_table} "
            "GROUP BY description ORDER BY revenue DESC LIMIT 20"
        )
    elif group_by:
        order_column = "trips" if topic == 4 else "avg_salary" if topic == 5 else "均價萬"
        stats_sql = (
            f"SELECT {stats_select} FROM {stats_table} "
            f"GROUP BY {group_by} ORDER BY {order_column} DESC LIMIT 20"
        )
    elif topic == 2:
        stats_sql = f"SELECT {stats_select} FROM {stats_table} ORDER BY ABS(price_diff) DESC LIMIT 20"
    else:
        stats_sql = f"SELECT {stats_select} FROM {stats_table} ORDER BY streams DESC LIMIT 20"

    return f'''
from fastapi import FastAPI

api = FastAPI(title={title!r})

@api.get("/health")
def health():
    return {{"status": "ok"}}

@api.get("/stats")
def stats():
    c = sqlite3.connect("pipeline.db")
    df_api = pd.read_sql("""{stats_sql}""", c)
    c.close()
    return df_api.to_dict(orient="records")

@api.get("/analyzed")
def analyzed():
    c = sqlite3.connect("pipeline.db")
    df_api = pd.read_sql("""SELECT {analyzed_select} FROM {analyzed_table} LIMIT 20""", c)
    c.close()
    return df_api.to_dict(orient="records")

print("✅ API 定義完成")
print("📡 /health:", health())
print("📡 /stats:", stats()[:3])
print("📡 /analyzed:", analyzed()[:3])
'''


def build_student_filled_starter(work_repo: Path, topic: int) -> Path:
    starter_path = work_repo / "data" / "raw" / f"topic_{topic}" / "pipeline_starter.ipynb"
    data = json.loads(starter_path.read_text())
    cells = code_cells(data)
    solution = solution_code_sources(work_repo, topic)

    if topic == 1:
        mapping = {
            1: 0,
            2: 1,
            3: 2,
            4: 3,
            5: 4,
            6: 5,
            7: 6,
            8: 7,
            9: 8,
            10: 9,
            12: 11,
            13: 12,
            14: 13,
            15: 14,
            16: 15,
            17: 16,
            18: 17,
            19: 18,
            21: 21,
            22: 22,
        }
        for starter_index, solution_index in mapping.items():
            set_cell_source(cells[starter_index], solution[solution_index])
        set_cell_source(cells[20], solution[19] + "\n" + solution[20])
        set_cell_source(cells[24], direct_api_demo_code(topic))
        set_cell_source(cells[25], 'print("API 已用 handler 直接驗證；正式 uvicorn 由整合測試檢查")')
        set_cell_source(cells[26], 'print("Dashboard 為回家作業，端到端測試略過互動 widget")')
    else:
        mapping = {
            1: 0,
            2: 1,
            3: 2,
            4: 3,
            5: 4,
            6: 5,
            7: 6,
            8: 7,
            9: 8,
            11: 10,
            12: 11,
            13: 12,
            14: 13,
            16: 14,
            17: 15,
            18: 16,
            20: 19,
            21: 20,
        }
        for starter_index, solution_index in mapping.items():
            set_cell_source(cells[starter_index], solution[solution_index])
        set_cell_source(cells[15], 'own_stats = pd.read_sql("SELECT COUNT(*) as rows FROM sqlite_master", conn)\nown_stats')
        set_cell_source(cells[19], solution[17] + "\n" + solution[18])
        set_cell_source(cells[23], direct_api_demo_code(topic))
        set_cell_source(cells[24], 'print("API 已用 handler 直接驗證；正式 uvicorn 由整合測試檢查")')
        set_cell_source(cells[25], 'print("重複練習題已於 Section 3 完成，端到端測試略過")')

    output = starter_path.with_name("student_filled.ipynb")
    output.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    return output


def execute_student_filled_starter(work_repo: Path, topic: int, logs_dir: Path) -> None:
    topic_dir = work_repo / "data" / "raw" / f"topic_{topic}"
    notebook = build_student_filled_starter(work_repo, topic)
    output = logs_dir / f"topic_{topic}_student_filled_executed.ipynb"
    run(
        [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            notebook.name,
            "--output",
            str(output),
            "--ExecutePreprocessor.timeout=180",
        ],
        cwd=topic_dir,
        log_path=logs_dir / f"topic_{topic}_student_filled.log",
    )


def table_counts(db_path: Path, tables: list[str]) -> dict[str, int]:
    conn = sqlite3.connect(db_path)
    try:
        return {
            table: int(conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])
            for table in tables
        }
    finally:
        conn.close()


def table_columns(db_path: Path, table: str) -> list[str]:
    conn = sqlite3.connect(db_path)
    try:
        return [row[1] for row in conn.execute(f"PRAGMA table_info({table})")]
    finally:
        conn.close()


def fetch_json(port: int, endpoint: str) -> tuple[int, object]:
    url = f"http://127.0.0.1:{port}{endpoint}"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            body = response.read().decode("utf-8")
            return response.status, json.loads(body)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            payload: object = json.loads(body)
        except json.JSONDecodeError:
            payload = body
        return exc.code, payload
    except urllib.error.URLError as exc:
        return 0, str(exc)


def wait_for_server(port: int, proc: subprocess.Popen[str]) -> None:
    for _ in range(30):
        if proc.poll() is not None:
            raise RuntimeError(f"uvicorn exited early with code {proc.returncode}")
        status, _payload = fetch_json(port, "/health")
        if status == 200:
            return
        time.sleep(0.3)
    raise RuntimeError(f"API did not become ready on port {port}")


def test_api(work_repo: Path, topic: int, logs_dir: Path) -> dict[str, int]:
    topic_dir = work_repo / "data" / "raw" / f"topic_{topic}"
    port = 8500 + topic
    log_file = (logs_dir / f"topic_{topic}_api.log").open("w")
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "api:app", "--host", "127.0.0.1", "--port", str(port)],
        cwd=topic_dir,
        stdout=log_file,
        stderr=subprocess.STDOUT,
        text=True,
    )
    try:
        wait_for_server(port, proc)
        endpoints = COMMON_ENDPOINTS + TOPICS[topic].get("extra_endpoints", [])
        statuses: dict[str, int] = {}
        for endpoint in endpoints:
            status, payload = fetch_json(port, endpoint)
            statuses[endpoint] = status
            if status != 200:
                raise RuntimeError(f"topic_{topic} {endpoint} returned {status}: {payload}")
            if endpoint == "/report":
                report = str(payload.get("report", "") if isinstance(payload, dict) else payload)
                if "{chr(10).join" in report:
                    raise RuntimeError(f"topic_{topic} report still contains unevaluated f-string code")
        return statuses
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
        log_file.close()


def main() -> int:
    root = repo_root()
    with tempfile.TemporaryDirectory(prefix="midterm-topics-") as tmp:
        work_repo = Path(tmp) / "midterm-mvp-template"
        logs_dir = Path(tmp) / "logs"
        logs_dir.mkdir()
        copy_repo(root, work_repo)

        for topic, config in TOPICS.items():
            print(f"topic_{topic}: validating starter notebook")
            validate_starter_notebook(work_repo, topic)

            print(f"topic_{topic}: executing student-filled starter notebook")
            execute_student_filled_starter(work_repo, topic, logs_dir)

            print(f"topic_{topic}: executing solution notebook")
            execute_notebook(work_repo, topic, logs_dir)

            topic_dir = work_repo / "data" / "raw" / f"topic_{topic}"
            counts = table_counts(topic_dir / "pipeline.db", config["tables"])
            if any(count <= 0 for count in counts.values()):
                raise RuntimeError(f"topic_{topic} has empty table counts: {counts}")
            analyzed_table = config["tables"][-1]
            columns = table_columns(topic_dir / "pipeline.db", analyzed_table)
            missing_columns = [column for column in config["analyzed_columns"] if column not in columns]
            if missing_columns:
                raise RuntimeError(f"topic_{topic} {analyzed_table} missing columns: {missing_columns}")
            if not (topic_dir / "output" / "pipeline_doc.md").exists():
                raise RuntimeError(f"topic_{topic} missing output/pipeline_doc.md")

            statuses = test_api(work_repo, topic, logs_dir)
            print(f"topic_{topic}: ok tables={counts} endpoints={statuses}")

    print("all midterm topics passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
