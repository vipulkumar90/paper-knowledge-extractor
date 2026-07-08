import os
from pathlib import Path

from dotenv import load_dotenv

# Project root
BASE_DIR = Path(__file__).resolve().parent

# Load local environment variables
load_dotenv(BASE_DIR / ".env")

# Logging
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILENAME: str = os.getenv("LOG_FILENAME", "research_knowledge.log").lower()

# Database Provider
DATABASE_PROVIDER = (
    os.getenv(
        "DATABASE_PROVIDER",
        "sqlite",
    )
    .strip()
    .lower()
)

# SQLite
SQLITE_DATABASE_PATH = os.getenv(
    "SQLITE_DATABASE_PATH",
    "data/facts.db",
)

# PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "")
POSTGRES_USER = os.getenv("POSTGRES_USER", "")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
POSTGRES_SSLMODE = os.getenv(
    "POSTGRES_SSLMODE",
    "require",
)
