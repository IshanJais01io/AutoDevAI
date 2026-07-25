from llm.config import LLM_PROVIDER

from llm.openai_provider import OpenAIProvider
from llm.gemini_provider import GeminiProvider



class LLMProvider:


    def __init__(self):

        if LLM_PROVIDER.lower() == "gemini":

            self.provider = GeminiProvider()

        else:

            self.provider = OpenAIProvider()



    def review(self, prompt):

        return self.provider.review(
            prompt
        )