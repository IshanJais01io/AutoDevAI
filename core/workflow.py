class Workflow:

    def __init__(self, memory):
        self.memory = memory
        self.agents = []


    def add_agent(self, agent):
        self.agents.append(agent)


    def run(self):

        for agent in self.agents:

            print(
                f"Running {agent.name}"
            )

            agent.run(self.memory)