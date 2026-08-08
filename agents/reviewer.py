from core.review_engine import ReviewEngine
from services.llm_service import LLMService
from core.settings import MAX_REVIEW_FILES


class ReviewerAgent:

    def __init__(self):

        self.name = "Reviewer Agent"

        self.provider = LLMService()

    def run(self, memory):

        repo_path = memory.get("repo_path")

        files = memory.get("files")

        print("Reviewing code...")

        python_files = [
            file
            for file in files
            if file.endswith(".py")
        ]

        total_python_files = len(
            python_files
        )

        if MAX_REVIEW_FILES is not None:

            python_files = python_files[
                :MAX_REVIEW_FILES
            ]

            print(
                f"Development Mode Enabled ({len(python_files)}/{total_python_files} Python files)"
            )

        engine = ReviewEngine(
            repo_path=repo_path,
            files=python_files
        )

        batches = engine.create_batches()

        reports = []

        total_batches = len(
            batches
        )

        for index, batch in enumerate(
            batches,
            start=1
        ):

            print(
                f"Reviewing batch {index}/{total_batches}"
            )

            prompt = engine.build_prompt(
                batch
            )

            try:

                review = self.provider.review(
                    prompt
                )

            except Exception as e:

                review = (
                    "Batch Review Failed\n\n"
                    f"{e}"
                )

            reports.append(
                "=" * 80
                + f"\nBATCH {index}\n"
                + "=" * 80
                + "\n\n"
                + review
                + "\n"
            )

        memory.update(
            "review_report",
            "\n".join(
                reports
            )
        )

        print(
            "Code review completed"
        )