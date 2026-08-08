from crewai import Crew
from crewai import Process

from crew.agents import CrewAgents
from crew.tasks import CrewTasks


class AutoDevCrew:

    def __init__(self):

        self.agent_factory = CrewAgents()

        self.task_factory = CrewTasks()

    def build(self, repository):

        planner = self.agent_factory.planner()

        reviewer = self.agent_factory.reviewer()

        tester = self.agent_factory.tester()

        documentation = self.agent_factory.documentation()

        security = self.agent_factory.security()

        final_report = self.agent_factory.final_report()

        tasks = [

            self.task_factory.planner_task(
                planner,
                repository
            ),

            self.task_factory.reviewer_task(
                reviewer
            ),

            self.task_factory.tester_task(
                tester
            ),

            self.task_factory.security_task(
                security
            ),

            self.task_factory.documentation_task(
                documentation
            ),

            self.task_factory.final_report_task(
                final_report
            )

        ]

        return Crew(

            agents=[

                planner,

                reviewer,

                tester,

                security,

                documentation,

                final_report

            ],

            tasks=tasks,

            process=Process.sequential,

            verbose=True

        )