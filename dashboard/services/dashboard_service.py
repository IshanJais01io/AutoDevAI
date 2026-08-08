from core.finding_engine import FindingEngine
from core.recommendation_engine import RecommendationEngine
from storage.models import get_latest_scan


class DashboardService:

    @staticmethod
    def build_dashboard_data():

        latest = get_latest_scan()

        if latest is None:

            return {
                "repository": "",
                "language": "",
                "files": 0,
                "score": 0,
                "security": 0,
                "testing": 0,
                "documentation": 0,
                "performance": 0,
                "health": 0,
                "recommendations": [],
                "findings": [],
            }

        health = round(
            (
                latest["score"]
                + latest["security"]
                + latest["testing"]
                + latest["documentation"]
            )
            / 4
        )

        performance = max(
            0,
            min(
                100,
                latest["score"] - 5
            )
        )

        recommendations = RecommendationEngine.generate(
            {
                "score": latest["score"],
                "security": latest["security"],
                "testing": latest["testing"],
                "documentation": latest["documentation"],
            }
        )

        findings = FindingEngine.generate(
            latest["repository"]
        )

        return {
            "repository": latest["repository"],
            "language": latest["language"],
            "files": latest["files"],
            "score": latest["score"],
            "security": latest["security"],
            "testing": latest["testing"],
            "documentation": latest["documentation"],
            "performance": performance,
            "health": health,
            "recommendations": recommendations,
            "findings": findings,
        }