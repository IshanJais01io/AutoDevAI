from crewai import Agent

from llm.provider import LLMProvider


class CrewAgents:

    def __init__(self):

        self.provider = LLMProvider()

    def planner(self):

        return Agent(
            role="Software Project Planner",
            goal="Analyze a GitHub repository and create a structured development plan.",
            backstory=(
                "You are a senior software architect responsible for "
                "understanding unfamiliar repositories and planning work."
            ),
            verbose=True,
            allow_delegation=False
        )

    def reviewer(self):

        return Agent(
            role="Senior Code Reviewer",
            goal="Review Python source code and identify bugs, code smells, security issues and improvements.",
            backstory=(
                "You are an experienced Staff Software Engineer performing "
                "production-quality code reviews."
            ),
            verbose=True,
            allow_delegation=False
        )

    def tester(self):

        return Agent(
            role="QA Automation Engineer",
            goal="Execute automated tests and summarize results.",
            backstory=(
                "You specialize in software quality assurance and automated testing."
            ),
            verbose=True,
            allow_delegation=False
        )

    def documentation(self):

        return Agent(
            role="Technical Documentation Engineer",
            goal="Generate professional technical documentation.",
            backstory=(
                "You write production-ready technical documentation for engineering teams."
            ),
            verbose=True,
            allow_delegation=False
        )

    def security(self):

        return Agent(
            role="Application Security Engineer",
            goal="Identify security vulnerabilities and risky coding practices.",
            backstory=(
                "You specialize in secure software development and static analysis."
            ),
            verbose=True,
            allow_delegation=False
        )

    def final_report(self):

        return Agent(
            role="Engineering Manager",
            goal="Prepare the final engineering report from all agent outputs.",
            backstory=(
                "You consolidate findings into a professional software engineering report."
            ),
            verbose=True,
            allow_delegation=False
        )