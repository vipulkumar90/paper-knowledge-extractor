# Paper Knowledge Extractor

A lightweight Python application for converting research papers into structured, machine-readable knowledge.

The project is designed to process hundreds or even thousands of research papers with minimal manual intervention. Rather than building a complex framework, the focus is on creating a reliable, easy-to-debug pipeline that extracts structured information from scientific literature using local Large Language Models (LLMs).

## Goals

* Convert PDF research papers into Markdown.
* Extract structured research knowledge using a local LLM.
* Validate extracted data using Pydantic.
* Store results in SQLite for later analysis.
* Process entire directories of papers automatically.
* Continue processing even if individual papers fail.

## Pipeline

```text
paper.pdf
    ↓
Marker
    ↓
Markdown
    ↓
Section-aware Chunking
    ↓
Local LLM
    ↓
Structured JSON
    ↓
Pydantic Validation
    ↓
Merge Chunk Results
    ↓
SQLite Database
```

## Features

* Batch processing of entire folders
* Marker-based PDF to Markdown conversion
* Section-aware Markdown chunking
* OpenAI-compatible local LLM support
* Configurable extraction prompts
* Automatic JSON validation with Pydantic
* Automatic repair retry for invalid responses
* SQLite storage for extracted knowledge
* Structured logging
* Fault-tolerant processing that continues after failures
* JSON export for each processed paper

## Technology Stack

* Python 3.12+
* Marker
* OpenAI Python SDK
* Local LLMs (Qwen3 14B / 32B Instruct)
* Pydantic
* SQLite
* python-dotenv
* tiktoken
* Standard Python logging

## Project Structure

```text
paper-knowledge-extractor/

├── app.py                      # Application entry point
├── requirements.txt
├── README.md
├── .env
├── .env.example
│
├── config/
│   └── settings.py             # Application configuration
│
├── core/
│   ├── marker_parser.py        # PDF → Markdown conversion
│   ├── chunking.py             # Markdown chunking
│   ├── llm.py                  # OpenAI-compatible LLM client
│   ├── extractor.py            # Extraction + validation pipeline
│   └── merger.py               # Merge chunk-level results
│
├── database/
│   ├── database.py             # SQLite operations
│   └── schema.sql              # Database schema
│
├── prompts/
│   ├── extraction.py           # Extraction prompt templates
│   └── repair.py               # JSON repair prompt templates
│
├── schemas/
│   ├── models.py               # Shared Pydantic models
│   └── research_schema.py      # Research extraction schema
│
├── utils/
│   ├── logger.py               # Logging configuration
│   ├── file_utils.py           # File helper functions
│   └── json_utils.py           # JSON helper functions
│
├── papers/                     # Input PDF files
│
├── output/
│   ├── markdown/               # Generated Markdown files
│   ├── chunks/                 # Chunked Markdown (debugging)
│   ├── extracted/              # Final extracted JSON
│   └── failed/                 # Failed responses and validation errors
│
├── logs/                       # Application logs
│
└── tests/                      # Unit and integration tests
```

## Directory Overview

| Directory     | Purpose                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------ |
| **config/**   | Centralized application configuration and environment settings.                            |
| **core/**     | The main processing pipeline responsible for parsing, chunking, extraction, and merging.   |
| **database/** | SQLite database initialization and persistence logic.                                      |
| **prompts/**  | LLM prompt templates separated from application logic for easy iteration.                  |
| **schemas/**  | Pydantic models and structured extraction schemas used for validation.                     |
| **utils/**    | Small reusable helper functions and logging utilities.                                     |
| **papers/**   | Input directory containing research paper PDFs.                                            |
| **output/**   | Generated Markdown, intermediate chunks, extracted JSON, and failed outputs for debugging. |
| **logs/**     | Runtime logs for monitoring and troubleshooting.                                           |
| **tests/**    | Unit and integration tests for the application.                                            |

## Design Philosophy

This project intentionally avoids unnecessary abstraction.

The primary objective is building a working research tool quickly while keeping the codebase clean, readable, and easy to maintain. Instead of introducing enterprise architecture, dependency injection, or plugin systems, each module has a single responsibility and can be understood independently.

## Future Plans

* Support additional local and cloud LLMs
* Improved Markdown chunking strategies
* Incremental processing of previously analyzed papers
* Parallel batch processing
* Multi-schema extraction for different research domains
* Embedding generation for semantic search
* Advanced merge strategies across chunks
* Export to PostgreSQL and DuckDB
* Interactive web dashboard for browsing extracted papers
* Vector database integration for Retrieval-Augmented Generation (RAG)
