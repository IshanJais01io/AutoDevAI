import os

from tools.test_runner import TestRunner


class TesterAgent:

    def __init__(self):

        self.name = "Tester Agent"

    def run(self, memory):

        repo_path = memory.get(
            "repo_path"
        )

        print(
            "Running tests..."
        )

        runner = TestRunner(
            repo_path
        )

        result = runner.run()

        report = self.generate_report(
            result
        )

        self.save_report(
            report
        )

        memory.update(
            "test_report",
            report
        )

        print(
            "Testing completed"
        )

    def generate_report(
        self,
        result
    ):

        lines = []

        lines.append(
            "# Testing Report"
        )

        lines.append("")

        if not result["success"]:

            lines.append(
                "Status: FAILED"
            )

            lines.append("")

            lines.append(
                result["stderr"]
            )

            return "\n".join(
                lines
            )

        status = (
            "PASSED"
            if result["return_code"] == 0
            else "FAILED"
        )

        lines.append(
            f"Status: {status}"
        )

        lines.append("")

        lines.append(
            f"Exit Code: {result['return_code']}"
        )

        lines.append("")

        lines.append(
            "## Pytest Output"
        )

        lines.append("")

        lines.append(
            result["stdout"]
        )

        if result["stderr"]:

            lines.append("")

            lines.append(
                "## Errors"
            )

            lines.append("")

            lines.append(
                result["stderr"]
            )

        return "\n".join(
            lines
        )

    def save_report(
        self,
        report
    ):

        os.makedirs(
            "reports",
            exist_ok=True
        )

        report_path = os.path.join(
            "reports",
            "testing_report.md"
        )

        with open(
            report_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                report
            )