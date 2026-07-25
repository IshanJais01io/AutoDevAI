import subprocess


class TestRunner:

    def __init__(self, repo_path):

        self.repo_path = repo_path

    def run(self):

        command = [
            "pytest",
            self.repo_path,
            "-q"
        ]

        try:

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False
            )

            return {
                "success": True,
                "return_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }

        except FileNotFoundError:

            return {
                "success": False,
                "return_code": -1,
                "stdout": "",
                "stderr": (
                    "pytest is not installed.\n"
                    "Run:\n"
                    "pip install pytest"
                )
            }

        except Exception as e:

            return {
                "success": False,
                "return_code": -1,
                "stdout": "",
                "stderr": str(e)
            }