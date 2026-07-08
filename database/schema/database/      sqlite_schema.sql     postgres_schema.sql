CREATE TABLE IF NOT EXISTS papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- File information
    filename TEXT NOT NULL UNIQUE,
    paper_title TEXT,
    markdown_path TEXT,
    json_path TEXT,

    -- Pipeline status
    status TEXT NOT NULL DEFAULT 'PENDING',

    -- Processing metadata
    chunk_count INTEGER DEFAULT 0,
    model_name TEXT,
    processing_time_ms INTEGER,

    -- Results
    extracted_json TEXT,

    -- Errors
    validation_errors TEXT,
    error_message TEXT,

    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);