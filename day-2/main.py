from utils.read_write import ReadWrite
from report_analysis import ReportAnalysis


def main():
    # format, rows of ids, columns seperated by a single space.
    reports = ReadWrite.read_file_rows_numbers("day-2/input/input.txt", " ")
    ReadWrite.write(
        "day-2/output/output.txt", [ReportAnalysis(reports).get_safe_report_count()]
    )


if __name__ == "__main__":
    main()
