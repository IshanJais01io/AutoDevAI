import os


class HTMLReportAgent:

    def __init__(self):

        self.name = "HTML Report Agent"

    def run(self, memory):

        os.makedirs(
            "reports",
            exist_ok=True
        )

        html = self.build_html(
            memory
        )

        with open(
            "reports/final_report.html",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)

        print("HTML report generated")

    def build_html(self, memory):

        return f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>AutoDevAI Report</title>

<style>

body {{
    font-family: Arial;
    margin:40px;
    background:#f4f4f4;
}}

.card {{
    background:white;
    padding:20px;
    border-radius:10px;
    margin-bottom:20px;
    box-shadow:0 0 8px rgba(0,0,0,.1);
}}

pre {{
    white-space:pre-wrap;
}}

</style>

</head>

<body>

<div class="card">

<h1>AutoDevAI Report</h1>

<p><b>Repository:</b> {memory.get("repo_path")}</p>

<p><b>Language:</b> {memory.get("language")}</p>

<p><b>Total Files:</b> {len(memory.get("files") or [])}</p>

</div>

<div class="card">

<h2>Review</h2>

<pre>{memory.get("review_report")}</pre>

</div>

<div class="card">

<h2>Testing</h2>

<pre>{memory.get("test_report")}</pre>

</div>

<div class="card">

<h2>Security</h2>

<pre>{memory.get("security_report")}</pre>

</div>

<div class="card">

<h2>Documentation</h2>

<pre>{memory.get("documentation_report")}</pre>

</div>

</body>

</html>
"""