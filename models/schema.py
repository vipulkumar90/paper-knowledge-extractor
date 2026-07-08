from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Author(BaseModel):
    """Author information."""

    name: str | None = None
    affiliation: str | None = None


class Dataset(BaseModel):
    """Dataset used in the paper."""

    name: str | None = None
    description: str | None = None


class Metric(BaseModel):
    """Evaluation metric."""

    name: str | None = None
    value: str | None = None


class Experiment(BaseModel):
    """Experiment performed in the paper."""

    name: str |None = None
    description: str | None = None
    metrics: list[Metric] = Field(default_factory=list)


class Paper(BaseModel):
    """
    Structured research knowledge extracted from a single paper.

    This model represents ONLY the JSON produced by the LLM.
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        validate_assignment=True,
    )

    title: str | None = None
    abstract: str | None = None

    authors: list[Author] = Field(default_factory=list)

    keywords: list[str] = Field(default_factory=list)

    research_problem: str | None = None
    methodology: str | None = None

    datasets: list[Dataset] = Field(default_factory=list)

    experiments: list[Experiment] = Field(default_factory=list)

    conclusions: str | None = None
    limitations: str | None = None
    future_work: str | None = None

    references: list[str] = Field(default_factory=list)

    metadata: dict[str, Any] = Field(default_factory=dict)