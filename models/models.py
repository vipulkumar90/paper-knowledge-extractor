from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path


class ProcessingStatus(StrEnum):
    """Processing status of a paper."""

    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass(slots=True)
class PaperFile:
    """
    Represents an input PDF file.
    """

    path: Path
    filename: str


@dataclass(slots=True)
class Chunk:
    """
    Represents a chunk of markdown sent to the LLM.
    """

    index: int
    text: str


@dataclass(slots=True)
class ProcessingResult:
    """
    Result of processing a single paper.
    """

    filename: str

    status: ProcessingStatus

    markdown_path: Path | None = None
    json_path: Path | None = None

    chunk_count: int = 0

    processing_time: float = 0.0

    error_message: str | None = None

    validation_errors: list[str] = field(default_factory=list)