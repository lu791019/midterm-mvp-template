from src.extract import extract_reviews
from src.llm_analyze import add_llm_analysis, write_report
from src.load import save_processed
from src.transform import transform_reviews


def main() -> None:
    raw_df = extract_reviews()
    cleaned_df = transform_reviews(raw_df)
    analyzed_df = add_llm_analysis(cleaned_df)
    data_path = save_processed(analyzed_df)
    report_path = write_report(analyzed_df)

    print(f"Processed data written to: {data_path}")
    print(f"Report written to: {report_path}")


if __name__ == "__main__":
    main()
