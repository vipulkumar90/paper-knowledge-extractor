# database/initializer.py

from pathlib import Path

from utils.config import DATABASE_PROVIDER, SQLITE_SCHEMA_FILENAME
from database.connection import database_exists, get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


SCHEMA_DIR = Path(__file__).parent / "schema"

if DATABASE_PROVIDER == "sqlite":
    SCHEMA_PATH = SCHEMA_DIR / SQLITE_SCHEMA_FILENAME
else:
    SCHEMA_PATH = SCHEMA_DIR / "paper_postgres.sql"


def initialize_database() -> None:
    """
    Initialize the application's SQLite database.

    Startup behavior:
    1. Create the database if it does not exist.
    2. Create all required tables.
    """
    try:
        if DATABASE_PROVIDER == "sqlite":
            if not database_exists():
                logger.info("Database not found. Creating a new database.")

                _create_schema()

                logger.info("Database initialized successfully.")
            else:
                logger.info("Using existing SQLite database.")

        elif DATABASE_PROVIDER == "postgres":
            logger.info("Ensuring PostgreSQL schema exists.")
            _create_schema()
        else:
            raise ValueError(f"Unsupported DATABASE_PROVIDER: {DATABASE_PROVIDER}")

    except Exception:
        logger.exception("Database initialization failed.")
        raise


def _create_schema() -> None:
    """
    Execute the database schema SQL script.
    """
    try:
        logger.info("Creating database schema.")

        with get_connection() as connection:
            schema = SCHEMA_PATH.read_text(encoding="utf-8")
            cursor = connection.cursor()
            cursor.execute(schema)
            connection.commit()

        logger.info("Database schema created successfully.")

    except Exception:
        logger.exception("Failed to create database schema.")
        raise
