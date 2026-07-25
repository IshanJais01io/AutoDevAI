import os


class ReviewEngine:

    DEFAULT_EXTENSIONS = {
        ".py",
        ".md",
        ".txt",
        ".json",
        ".yaml",
        ".yml",
        ".toml",
        ".ini",
        ".cfg"
    }

    def __init__(
        self,
        repo_path,
        files,
        max_batch_characters=25000
    ):

        self.repo_path = repo_path
        self.files = files
        self.max_batch_characters = max_batch_characters

    def create_batches(self):

        batches = []

        current_batch = []

        current_size = 0

        for relative_path in self.files:

            if not self.is_reviewable(
                relative_path
            ):
                continue

            absolute_path = os.path.join(
                self.repo_path,
                relative_path
            )

            try:

                with open(
                    absolute_path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    content = file.read()

            except Exception:

                continue

            section = self.build_section(
                relative_path,
                content
            )

            section_size = len(section)

            if (
                current_batch
                and
                current_size + section_size
                > self.max_batch_characters
            ):

                batches.append(
                    current_batch
                )

                current_batch = []

                current_size = 0

            current_batch.append(section)

            current_size += section_size

        if current_batch:

            batches.append(
                current_batch
            )

        return batches

    def build_prompt(
        self,
        batch
    ):

        return (
            "You are a Senior Software Engineer.\n\n"
            "Perform a production-grade repository review.\n\n"
            "Review every file carefully.\n\n"
            "Focus on:\n"
            "- Bugs\n"
            "- Code Quality\n"
            "- Architecture\n"
            "- Performance\n"
            "- Security\n"
            "- Best Practices\n"
            "- Maintainability\n"
            "- Refactoring Suggestions\n\n"
            "Return the review in Markdown.\n\n"
            + "\n\n".join(batch)
        )

    def build_section(
        self,
        filename,
        content
    ):

        return (
            f"FILE: {filename}\n\n"
            f"{content}"
        )

    def is_reviewable(
        self,
        filename
    ):

        extension = os.path.splitext(
            filename
        )[1].lower()

        return extension in self.DEFAULT_EXTENSIONS