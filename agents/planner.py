import os


class PlannerAgent:

    IGNORE_DIRECTORIES = {
        ".git",
        ".github",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".idea",
        ".vscode",
        "venv",
        ".venv",
        "env",
        "node_modules",
        "dist",
        "build",
        ".coverage"
    }

    IGNORE_EXTENSIONS = {
        ".pyc",
        ".pyo",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".bmp",
        ".ico",
        ".svg",
        ".pdf",
        ".zip",
        ".tar",
        ".gz",
        ".rar",
        ".7z",
        ".exe",
        ".dll",
        ".so",
        ".class",
        ".jar",
        ".mp3",
        ".wav",
        ".mp4",
        ".avi",
        ".mov",
        ".log"
    }

    def __init__(self):

        self.name = "Planner Agent"

    def run(self, memory):

        repo_path = memory.get("repo_path")

        print("Analyzing repository...")

        files = self.scan_repository(
            repo_path
        )

        language = self.detect_language(
            files
        )

        memory.update(
            "files",
            files
        )

        memory.update(
            "language",
            language
        )

        print(f"Discovered {len(files)} project files")

        print("Repository analysis completed")

    def scan_repository(self, repo_path):

        project_files = []

        for root, directories, filenames in os.walk(repo_path):

            directories[:] = [
                directory
                for directory in directories
                if directory not in self.IGNORE_DIRECTORIES
            ]

            for filename in filenames:

                _, extension = os.path.splitext(
                    filename
                )

                if extension.lower() in self.IGNORE_EXTENSIONS:
                    continue

                absolute_path = os.path.join(
                    root,
                    filename
                )

                relative_path = os.path.relpath(
                    absolute_path,
                    repo_path
                )

                project_files.append(
                    relative_path
                )

        project_files.sort()

        return project_files

    def detect_language(self, files):

        python_files = [
            file
            for file in files
            if file.endswith(".py")
        ]

        if python_files:
            return "Python"

        return "Unknown"