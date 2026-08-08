from typing import List, Dict


class RecommendationEngine:

    @staticmethod
    def generate(report: Dict) -> List[Dict]:

        recommendations = []

        security = report.get("security", 100)
        testing = report.get("testing", 100)
        documentation = report.get("documentation", 100)
        score = report.get("score", 100)

        # ---------- Security ----------

        if security < 100:

            recommendations.append({

                "priority": "Critical",

                "title": "Strengthen Security",

                "description": "Review vulnerable code paths and replace unsafe database or filesystem operations.",

                "category": "Security",

                "impact": "Very High",

                "eta": "15 mins"

            })

        # ---------- Testing ----------

        if testing < 95:

            recommendations.append({

                "priority": "High",

                "title": "Increase Test Coverage",

                "description": "Add unit tests for uncovered functions and edge cases.",

                "category": "Testing",

                "impact": "High",

                "eta": "20 mins"

            })

        if testing < 85:

            recommendations.append({

                "priority": "High",

                "title": "Improve Integration Tests",

                "description": "Critical workflows should be validated with integration tests.",

                "category": "Testing",

                "impact": "High",

                "eta": "30 mins"

            })

        # ---------- Documentation ----------

        if documentation < 100:

            recommendations.append({

                "priority": "Medium",

                "title": "Improve Documentation",

                "description": "Document public APIs and update README examples.",

                "category": "Documentation",

                "impact": "Medium",

                "eta": "10 mins"

            })

        # ---------- Code Quality ----------

        if score < 95:

            recommendations.append({

                "priority": "Medium",

                "title": "Reduce Code Complexity",

                "description": "Split large methods into reusable helper functions.",

                "category": "Code Quality",

                "impact": "Medium",

                "eta": "25 mins"

            })

        # ---------- Best Practices ----------

        defaults = [

            ("Add Python Type Hints",
             "Improve IDE support and maintainability.",
             "Maintainability"),

            ("Improve Exception Handling",
             "Replace generic exception handlers with specific exceptions.",
             "Reliability"),

            ("Optimize Imports",
             "Remove unused imports and organize modules.",
             "Performance"),

            ("Refactor Long Functions",
             "Break large functions into smaller reusable units.",
             "Maintainability"),

            ("Reduce Duplicate Logic",
             "Extract common logic into shared utilities.",
             "Maintainability"),

            ("Improve Logging",
             "Add structured logging for production debugging.",
             "Monitoring"),

            ("Optimize Repository Structure",
             "Group related modules into packages.",
             "Architecture"),

            ("Review Naming Conventions",
             "Improve variable and function naming consistency.",
             "Readability"),

            ("Enable Static Analysis",
             "Run Ruff, Flake8 or Pylint during CI.",
             "Quality"),

            ("Enable Continuous Integration",
             "Run tests automatically on every push.",
             "DevOps"),

            ("Improve Dependency Management",
             "Pin dependency versions to improve reproducibility.",
             "Dependencies")

        ]

        index = 0

        while len(recommendations) < 12:

            title, description, category = defaults[index]

            recommendations.append({

                "priority": "Info",

                "title": title,

                "description": description,

                "category": category,

                "impact": "Low",

                "eta": "5 mins"

            })

            index += 1

            if index >= len(defaults):
                break

        return recommendations