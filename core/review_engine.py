from core.settings import MAX_BATCH_CHARACTERS
import os

from prompts.reviewer import build_review_prompt


class ReviewEngine:

    DEFAULT_EXTENSIONS = {
        ".py",
        ".js",
        ".ts",
        ".jsx",
        ".tsx",
        ".java",
        ".kt",
        ".go",
        ".rs",
        ".cpp",
        ".c",
        ".h",
        ".hpp",
        ".cs",
        ".php",
        ".rb",
        ".swift",
        ".scala",
        ".sql",
        ".html",
        ".css",
        ".scss",
        ".vue",
        ".json",
        ".yaml",
        ".yml",
        ".toml",
        ".ini",
        ".cfg",
        ".env",
        ".md",
        ".txt",
        ".xml",
        ".sh"
    }

    def __init__(
        self,
        repo_path,
        files,
        max_batch_characters=MAX_BATCH_CHARACTERS
    ):

        self.repo_path = repo_path
        self.files = sorted(files)
        self.max_batch_characters = max_batch_characters

    def create_batches(self):

        batches = []

        current_batch = []

        current_size = 0

        for relative_path in self.files:

            if not self.is_reviewable(relative_path):
                continue

            absolute_path = os.path.join(
                self.repo_path,
                relative_path
            )

            if not os.path.isfile(absolute_path):
                continue

            try:

                with open(
                    absolute_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as file:

                    content = file.read()

            except Exception:

                continue

            if not content.strip():
                continue

            section = self.build_section(
                relative_path,
                content
            )

            section_size = len(section)

            if (
                current_batch and
                current_size + section_size >
                self.max_batch_characters
            ):

                batches.append(current_batch)

                current_batch = []

                current_size = 0

            current_batch.append(section)

            current_size += section_size

        if current_batch:

            batches.append(current_batch)

        return batches

    def build_prompt(self, batch):

        return build_review_prompt(
            "\n\n".join(batch)
        )

    def build_section(
        self,
        filename,
        content
    ):

        return (
            "=" * 80 +
            "\nFILE: " +
            filename +
            "\n" +
            "=" * 80 +
            "\n\n" +
            content
        )

    def is_reviewable(
        self,
        filename
    ):

        extension = os.path.splitext(
            filename
        )[1].lower()

        return extension in self.DEFAULT_EXTENSIONS