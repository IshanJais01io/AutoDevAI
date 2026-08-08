from crewai import Task


class CrewTasks:

    def planner_task(self, agent, repository):

        return Task(

            description=f"""

Analyze the following GitHub repository.

Repository:

{repository}

Create:

1. Architecture Overview

2. Technology Stack

3. Folder Structure

4. Major Components

5. Improvement Suggestions

""",

            expected_output="Project Planning Report",

            agent=agent

        )

    def reviewer_task(self, agent):

        return Task(

            description="""

Review the repository.

Focus on:

- Code Quality

- Bugs

- Complexity

- Best Practices

- Refactoring Opportunities

""",

            expected_output="Professional Code Review Report",

            agent=agent

        )

    def tester_task(self, agent):

        return Task(

            description="""

Analyze project testing.

Identify:

- Missing Tests

- Existing Tests

- Coverage

- Test Recommendations

""",

            expected_output="Testing Report",

            agent=agent

        )

    def documentation_task(self, agent):

        return Task(

            description="""

Generate complete technical documentation.

Include:

- Overview

- Installation

- Usage

- Architecture

- Components

""",

            expected_output="Documentation Report",

            agent=agent

        )

    def security_task(self, agent):

        return Task(

            description="""

Analyze security.

Check:

- Secrets

- Hardcoded Credentials

- Unsafe Code

- Injection Risks

- Vulnerabilities

""",

            expected_output="Security Report",

            agent=agent

        )

    def final_report_task(self, agent):

        return Task(

            description="""

Generate one final engineering report.

Combine:

- Planning

- Review

- Testing

- Documentation

- Security

Provide:

Overall Project Score

Priority Issues

Recommended Next Steps

""",

            expected_output="Final Engineering Report",

            agent=agent

        )