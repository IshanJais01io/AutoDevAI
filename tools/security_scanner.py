import json
import subprocess


class SecurityScanner:

    def __init__(self, repo_path):

        self.repo_path = repo_path

    def scan(self):

        command = [
            "bandit",
            "-r",
            self.repo_path,
            "-f",
            "json"
        ]

        try:

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False
            )

        except FileNotFoundError:

            return {
                "success": False,
                "message": (
                    "Bandit is not installed.\n"
                    "Install it using:\n"
                    "pip install bandit"
                ),
                "results": []
            }

        if result.returncode not in (0, 1):

            return {
                "success": False,
                "message": result.stderr.strip(),
                "results": []
            }

        try:

            data = json.loads(result.stdout)

        except json.JSONDecodeError:

            return {
                "success": False,
                "message": "Unable to parse Bandit output.",
                "results": []
            }

        return {
            "success": True,
            "message": "Security scan completed.",
            "results": data.get("results", [])
        }