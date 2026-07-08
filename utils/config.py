import os
from pathlib import Path

from dotenv import load_dotenv

# Project root
BASE_DIR = Path(__file__).resolve().parent

# Load local environment variables
load_dotenv(BASE_DIR / ".env")

# Logging
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()
