# 題目 4：音樂串流趨勢分析

## 情境

你是一家音樂串流平台的資料顧問。產品經理說：「我想知道 2024 年哪些歌最紅、哪些藝人竄升最快、跨平台（Spotify/YouTube/TikTok）的表現有沒有差異，還有能不能自動生成推薦歌單的文案。」

## 你的角色

娛樂產業資料顧問

## 使用者

音樂串流平台產品經理——用分析結果決定首頁推薦、歌單企劃、藝人合作。

## 資料來源

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| `tracks.csv` | 2,000 | Spotify 2024 年最多串流歌曲（含跨平台數據） | [Kaggle: Most Streamed Spotify Songs 2024](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024) |

### 主要欄位（共 30 欄，列出關鍵欄位）

| 欄位 | 型別 | 說明 |
|------|------|------|
| `Track` | str | 歌名 |
| `Artist` | str | 藝人 |
| `Album Name` | str | 專輯名 |
| `Release Date` | str | 發行日期 |
| `All Time Rank` | int | 歷史排名 |
| `Spotify Streams` | str | Spotify 播放量（注意：含逗號，需轉數字） |
| `Spotify Playlist Count` | str | 被加入的播放清單數 |
| `YouTube Views` | str | YouTube 觀看數 |
| `TikTok Posts` | str | TikTok 使用次數 |
| `Explicit Track` | int | 是否為限制級 |

## 今日 MVP Scope

### ETL（pandas 清洗 + 統計）

- 數值欄位清洗（去逗號、轉 int/float）
- 統計：Top 20 歌曲排行、Top 10 藝人（依總播放量）
- 跨平台比較：Spotify vs YouTube vs TikTok 各自 Top 10
- 產出 `data/processed/music_trends.csv`

### LLM（AI 加值分析）

- 對 Top 10 歌曲生成**聽眾洞察**：為什麼這首歌紅？可能的原因？
- 生成**推薦歌單文案**：根據數據，寫一段 100 字的歌單推薦介紹
- 跨平台趨勢摘要：Spotify 紅但 TikTok 不紅的歌，可能代表什麼？

## 預期產出

- `data/processed/music_trends.csv`：清洗後的排行與統計
- `output/report.md`：趨勢分析 + 推薦歌單文案 + 跨平台洞察

## 成功指標

- 能說出「2024 年 Spotify 播放量最高的 3 首歌，在 YouTube 和 TikTok 的表現如何」
- LLM 生成的歌單文案自然、有吸引力
