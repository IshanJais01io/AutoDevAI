from google import genai
from google.genai import types

from llm.config import (
    GEMINI_KEY,
    GEMINI_MODEL,
    TEMPERATURE,
    MAX_TOKENS,
)

from llm.base_provider import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):

    def __init__(self):

        super().__init__()

        self.client = genai.Client(
            api_key=GEMINI_KEY
        )

    def review(self, prompt):

        def request():

            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=TEMPERATURE,
                    max_output_tokens=MAX_TOKENS,
                ),
            )

            return response.text

        return self.execute_with_retry(
            request
        )