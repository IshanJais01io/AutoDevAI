def build_planner_prompt(repository):

    return f"""
Analyze this repository.

Repository:

{repository}

Generate:

1. Architecture
2. Tech Stack
3. Components
4. Folder Structure
5. Recommendations
"""