import time
import logging
from abc import ABC, abstractmethod


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class BaseLLMProvider(ABC):

    def __init__(
        self,
        max_retries=3,
        retry_delay=2
    ):
        self.max_retries = max_retries
        self.retry_delay = retry_delay


    def execute_with_retry(self, function):

        last_error = None

        for attempt in range(self.max_retries):

            try:

                logging.info(
                    f"LLM request attempt {attempt + 1}"
                )

                return function()


            except Exception as error:

                last_error = error

                logging.warning(
                    f"Attempt {attempt + 1} failed: {error}"
                )


                if attempt < self.max_retries - 1:
                    time.sleep(
                        self.retry_delay
                    )


        logging.error(
            f"LLM request failed: {last_error}"
        )

        return (
            "LLM request failed. "
            f"Error: {last_error}"
        )


    @abstractmethod
    def review(self, prompt):
        pass