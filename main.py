from core.shared_memory import SharedMemory
from core.workflow import Workflow

from agents.planner import PlannerAgent
from agents.reviewer import ReviewerAgent
from agents.tester import TesterAgent
from agents.documentation import DocumentationAgent
from agents.security import SecurityAgent
from agents.final_report import FinalReportAgent

from tools.github import GitHubTool


memory = SharedMemory()

github = GitHubTool()


url = input(
    "Enter GitHub Repository URL: "
)


repo_path = github.clone_repository(
    url
)


memory.update(
    "repo_path",
    repo_path
)


workflow = Workflow(
    memory
)


planner = PlannerAgent()

reviewer = ReviewerAgent()

tester = TesterAgent()

documentation = DocumentationAgent()

security = SecurityAgent()

final_report = FinalReportAgent()


workflow.add_agent(
    planner
)

workflow.add_agent(
    reviewer
)

workflow.add_agent(
    tester
)

workflow.add_agent(
    documentation
)

workflow.add_agent(
    security
)

workflow.add_agent(
    final_report
)


workflow.run()


print("\n====================================")
print("AutoDevAI Execution Completed")
print("====================================")

print(
    f"Repository : {memory.get('repo_path')}"
)

print(
    f"Language   : {memory.get('language')}"
)

files = memory.get("files") or []

print(
    f"Files      : {len(files)}"
)

print()

print("Reports Generated")

print("-----------------")

print("Review Report         : Available")

print("Testing Report        : Available")

print("Documentation Report  : Available")

print("Security Report       : Available")

print("Final Report          : Available")

print()

print("Reports Folder")

print("-----------------")

print("reports/")
print("├── documentation_report.md")
print("├── testing_report.md")
print("├── security_report.md")
print("└── final_report.md")

print()

print("Workflow completed successfully.")