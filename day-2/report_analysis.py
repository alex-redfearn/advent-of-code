from math import copysign


class ReportAnalysis:

    def __init__(self, reports: list[list[int]]):
        self.reports = reports

    def get_safe_report_count(self):
        count = 0
        for report in self.reports:
            if self.__is_report_safe(report):
                count += 1

        return count

    def __is_report_safe(self, report):
        error_index = self.__return_error_index(report)

        attempt = 0
        while error_index != -1 and attempt < 3:
            # Attempt to first remove the error index, next iteration error index - 1, finally the error index + 1.
            modified_report = (
                report[: error_index + (attempt - 1)] + report[error_index + attempt :]
            )

            # If the modified report is now safe, mark as safe.
            if self.__return_error_index(modified_report) == -1:
                error_index = -1

            attempt += 1

        return error_index == -1

    def __return_error_index(self, report):
        error_index = -1
        previous_trend = 0

        for i in range(len(report) - 1):
            change = report[i + 1] - report[i]
            trend = int(copysign(1, change))

            # Any two adjacent levels differ by at least one and at most three.
            if abs(change) < 1 or abs(change) > 3:
                error_index = i
                break

            # The levels are either all increasing or all decreasing.
            if previous_trend != 0 and trend != previous_trend:
                error_index = i
                break

            previous_trend = trend

        return error_index
