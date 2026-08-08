import os
import re


class FindingEngine:

    @staticmethod
    def generate(repo_path):

        findings = []

        secret_patterns = [
            ("API Key", r"(?i)(api[_-]?key)\s*=\s*['\"].+['\"]"),
            ("Password", r"(?i)(password|passwd)\s*=\s*['\"].+['\"]"),
            ("Secret", r"(?i)(secret|token)\s*=\s*['\"].+['\"]"),
            ("AWS Key", r"AKIA[0-9A-Z]{16}")
        ]

        for root, _, files in os.walk(repo_path):

            for file in files:

                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                except Exception:
                    continue

                relative = os.path.relpath(path, repo_path)
                lines = text.splitlines()

                # eval()
                for line_number, line in enumerate(lines, start=1):
                    if "eval(" in line:
                        findings.append({
                            "severity": "High",
                            "file": relative,
                            "line": line_number,
                            "category": "Security",
                            "confidence": 99,
                            "recommendation": "Avoid using eval()."
                        })

                # exec()
                for line_number, line in enumerate(lines, start=1):
                    if "exec(" in line:
                        findings.append({
                            "severity": "High",
                            "file": relative,
                            "line": line_number,
                            "category": "Security",
                            "confidence": 98,
                            "recommendation": "Avoid using exec()."
                        })

                # Secrets
                for name, pattern in secret_patterns:
                    for line_number, line in enumerate(lines, start=1):
                        if re.search(pattern, line):
                            findings.append({
                                "severity": "High",
                                "file": relative,
                                "line": line_number,
                                "category": "Secrets",
                                "confidence": 97,
                                "recommendation": f"Possible hardcoded {name} detected."
                            })

                # TODO
                for line_number, line in enumerate(lines, start=1):
                    if "TODO" in line:
                        findings.append({
                            "severity": "Medium",
                            "file": relative,
                            "line": line_number,
                            "category": "Maintainability",
                            "confidence": 92,
                            "recommendation": "Resolve TODO comments."
                        })

                # Debug print
                for line_number, line in enumerate(lines, start=1):
                    if "print(" in line:
                        findings.append({
                            "severity": "Low",
                            "file": relative,
                            "line": line_number,
                            "category": "Code Quality",
                            "confidence": 88,
                            "recommendation": "Remove debug print statements."
                        })

                # Large file
                if len(lines) > 400:
                    findings.append({
                        "severity": "Medium",
                        "file": relative,
                        "line": 1,
                        "category": "Complexity",
                        "confidence": 90,
                        "recommendation": "Large file; consider splitting."
                    })

                # Missing docstrings
                if "def " in text and '"""' not in text:
                    findings.append({
                        "severity": "Low",
                        "file": relative,
                        "line": 1,
                        "category": "Documentation",
                        "confidence": 84,
                        "recommendation": "Consider adding docstrings."
                    })

        findings.sort(
            key=lambda x: (
                x["severity"] != "High",
                x["severity"] != "Medium"
            )
        )

        return findings[:100]