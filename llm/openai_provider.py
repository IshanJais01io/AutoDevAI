from openai import OpenAI

from llm.config import OPENAI_KEY, OPENAI_MODEL, TEMPERATURE, MAX_TOKENS
from llm.base_provider import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):

    def __init__(self):
        super().__init__()

        self.client = OpenAI(
            api_key=OPENAI_KEY
        )


    def review(self, prompt):

        def request():

            response = self.client.chat.completions.create(

                model=OPENAI_MODEL,

                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a senior software engineer "
                            "specialized in code review."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=TEMPERATURE,

                max_tokens=MAX_TOKENS
            )


            return response.choices[0].message.content


        return self.execute_with_retry(
            request
        )