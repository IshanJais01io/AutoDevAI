class ScoreEngine:

    def calculate(self, memory):

        review = memory.get("review_report") or ""
        testing = memory.get("test_report") or ""
        security = memory.get("security_report") or ""
        documentation = memory.get("documentation_report") or ""

        review_score = 100
        security_score = 100
        testing_score = 100
        documentation_score = 100

        # Review deductions
        review_score -= review.lower().count("high") * 5
        review_score -= review.lower().count("medium") * 3
        review_score -= review.lower().count("low") * 1

        # Security deductions
        security_score -= security.lower().count("critical") * 10
        security_score -= security.lower().count("high") * 5
        security_score -= security.lower().count("medium") * 3

        # Testing deductions
        testing_score -= testing.lower().count("failed") * 5

        # Documentation deductions
        documentation_score -= documentation.lower().count("missing") * 2

        review_score = max(0, review_score)
        security_score = max(0, security_score)
        testing_score = max(0, testing_score)
        documentation_score = max(0, documentation_score)

        overall = int(
            (
                review_score +
                security_score +
                testing_score +
                documentation_score
            ) / 4
        )

        return {

            "overall": overall,

            "security": security_score,

            "testing": testing_score,

            "documentation": documentation_score

        }