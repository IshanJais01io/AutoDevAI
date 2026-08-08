import json
import os


class JSONExportAgent:

    def __init__(self):

        self.name = "JSON Export Agent"

    def run(self, memory):

        os.makedirs(
            "reports",
            exist_ok=True
        )

        data = {

            "repository": memory.get("repo_path"),

            "language": memory.get("language"),

            "files": len(memory.get("files") or []),

            "review": memory.get("review_report"),

            "testing": memory.get("test_report"),

            "security": memory.get("security_report"),

            "documentation": memory.get("documentation_report")

        }

        with open(

            "reports/final_report.json",

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                data,

                file,

                indent=4,

                ensure_ascii=False

            )

        memory.update(

            "json_report",

            "reports/final_report.json"

        )

        print("JSON report generated")