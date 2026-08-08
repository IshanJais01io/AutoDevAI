import re


class ReviewParser:

    def parse(self, report):

        if not report:
            report = ""

        bugs = len(re.findall(r"\bbug\b", report, re.IGNORECASE))
        security = len(re.findall(r"\bsecurity\b", report, re.IGNORECASE))
        performance = len(re.findall(r"\bperformance\b", report, re.IGNORECASE))
        maintainability = len(re.findall(r"\bmaintain", report, re.IGNORECASE))

        score = 100

        score -= bugs * 5
        score -= security * 5
        score -= performance * 3
        score -= maintainability * 2

        score = max(0, min(score, 100))

        return {
            "score": score,
            "bugs": bugs,
            "security": security,
            "performance": performance,
            "maintainability": maintainability
        }