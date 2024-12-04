from unittest import TestCase
from report_analyser import ReportAnalyser


class TestReportAnalyser(TestCase):

    def test_given_report_with_zero_errors_when_analysed_returns_safe(self):
        report = [7, 6, 4, 2, 1]

        analyser = ReportAnalyser([report])

        count = analyser.get_safe_report_count()

        assert count == 1

    def test_given_report_with_unfixable_errors_when_analysed_returns_unsafe(self):
        reports = [
            [1, 2, 7, 8, 9],
            [94, 96, 94, 96, 96],
            [25, 28, 29, 26, 33],
            [49, 51, 53, 56, 56, 57, 55],
        ]

        analyser = ReportAnalyser(reports)

        count = analyser.get_safe_report_count()

        assert count == 0

    def test_given_reports_with_fixable_errors_when_analysed_returns_safe(self):
        # Current index equals the index the iterator is on when the error is discovered.

        # There are three different fixable error scenarios as listed below.
        report = [
            [28, 31, 33, 32, 33],  # fixed by removing current error index.
            [42, 44, 45, 44, 47, 50],  # fixed by removing current error index + 1.
            [69, 71, 69, 66, 63],  # fixed by removing current error index - 1.
        ]

        analyser = ReportAnalyser(report)

        count = analyser.get_safe_report_count()

        assert count == 3
