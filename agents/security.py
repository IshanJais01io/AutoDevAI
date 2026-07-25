import os

from tools.security_scanner import SecurityScanner


class SecurityAgent:

    def __init__(self):

        self.name = "Security Agent"

    def run(self, memory):

        repo_path = memory.get("repo_path")

        print("Running security scan...")

        scanner = SecurityScanner(
            repo_path
        )

        result = scanner.scan()

        report = self.generate_report(
            result
        )

        os.makedirs(
            "reports",
            exist_ok=True
        )

        report_path = os.path.join(
            "reports",
            "security_report.md"
        )

        with open(
            report_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        memory.update(
            "security_report",
            report
        )

        print(
            "Security report generated"
        )

    def generate_report(
        self,
        result
    ):

        lines = []

        lines.append(
            "# Security Report\n"
        )

        if not result["success"]:

            lines.append(
                "## Scan Status\n"
            )

            lines.append(
                result["message"]
            )

            return "\n".join(lines)

        findings = result["results"]

        lines.append(
            f"Total Issues Found: {len(findings)}\n"
        )

        if not findings:

            lines.append(
                "No security issues were found."
            )

            return "\n".join(lines)

        for index, issue in enumerate(
            findings,
            start=1
        ):

            lines.append(
                "---"
            )

            lines.append(
                f"## Issue {index}"
            )

            lines.append(
                f"Severity: {issue.get('issue_severity', 'Unknown')}"
            )

            lines.append(
                f"Confidence: {issue.get('issue_confidence', 'Unknown')}"
            )

            lines.append(
                f"File: {issue.get('filename', '')}"
            )

            lines.append(
                f"Line: {issue.get('line_number', '')}"
            )

            lines.append(
                f"Test: {issue.get('test_name', '')}"
            )

            lines.append(
                f"Description: {issue.get('issue_text', '')}"
            )

            lines.append("")

        return "\n".join(lines)