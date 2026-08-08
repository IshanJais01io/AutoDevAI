from llm.provider import LLMProvider


class LLMService:

    def __init__(self):

        self.provider = LLMProvider()

    def review(self, prompt):

        return self.provider.review(prompt)

    def ask(self, prompt):

        return self.provider.review(prompt)