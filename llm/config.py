import os

from dotenv import load_dotenv


load_dotenv()


# API KEYS

OPENAI_KEY = os.getenv(
    "OPENAI_API_KEY"
)

GEMINI_KEY = os.getenv(
    "GEMINI_API_KEY"
)


# ACTIVE PROVIDER

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "openai"
)


# MODEL CONFIGURATION

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-5.5"
)


GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-pro"
)


# GENERATION SETTINGS

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0.2"
    )
)


MAX_TOKENS = int(
    os.getenv(
        "MAX_TOKENS",
        "1500"
    )
)


# RETRY SETTINGS

MAX_RETRIES = int(
    os.getenv(
        "MAX_RETRIES",
        "3"
    )
)


REQUEST_TIMEOUT = int(
    os.getenv(
        "REQUEST_TIMEOUT",
        "60"
    )
)


# Development Mode
# None = Review all Python files
# Integer = Review only first N Python files