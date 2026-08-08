from core.shared_memory import SharedMemory
from core.workflow import Workflow
from storage.database import initialize_database
from core.pdf_report import generate_pdf
from agents.json_export import JSONExportAgent
from agents.html_report import HTMLReportAgent
from agents.planner import PlannerAgent
from agents.reviewer import ReviewerAgent
from agents.tester import TesterAgent
from agents.documentation import DocumentationAgent
from agents.security import SecurityAgent
from agents.final_report import FinalReportAgent

from tools.github import GitHubTool

from core.settings import (
    USE_CREWAI,
    initialize
)


def run_pipeline(repository_url: str):

    initialize_database()

    initialize()

    memory = SharedMemory()

    github = GitHubTool()

    repo_path = github.clone_repository(repository_url)

    memory.update(
        "repo_path",
        repo_path
    )

    if not USE_CREWAI:

        workflow = Workflow(memory)

        workflow.add_agent(PlannerAgent())
        workflow.add_agent(ReviewerAgent())
        workflow.add_agent(TesterAgent())
        workflow.add_agent(DocumentationAgent())
        workflow.add_agent(SecurityAgent())
        workflow.add_agent(FinalReportAgent())
        workflow.add_agent(JSONExportAgent())
        workflow.add_agent(HTMLReportAgent())

        workflow.run()
        generate_pdf()
        return memory.get_all()

    else:

        from crew.crew import AutoDevCrew

        crew = AutoDevCrew().build(
            repository=repo_path
        )

        result = crew.kickoff()

        memory.update(
            "crew_result",
            str(result)
        )

        generate_pdf()
        return memory.get_all()


if __name__ == "__main__":

    url = input(
        "Enter GitHub Repository URL: "
    )

    result = run_pipeline(url)

    print()

    print("=" * 60)

    print("FINAL MEMORY")

    print("=" * 60)

    print(result)