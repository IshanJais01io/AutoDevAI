from typing import List


class Workflow:

    def __init__(self, memory):

        self.memory = memory

        self.agents: List = []

    def add_agent(self, agent):

        self.agents.append(agent)

    def run(self):

        results = []

        for agent in self.agents:

            print(f"\n========== {agent.name} ==========")

            try:

                output = agent.run(self.memory)

                if output is not None:

                    self.memory[agent.name] = output

                results.append({

                    "agent": agent.name,

                    "status": "success"

                })

            except Exception as error:

                print(f"{agent.name} failed: {error}")

                results.append({

                    "agent": agent.name,

                    "status": "failed",

                    "error": str(error)

                })

        self.memory["workflow_results"] = results

        return self.memory