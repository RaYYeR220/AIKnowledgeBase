# Concept

A strong AI assistant should not depend entirely on the current chat window.
It should be able to:
- recover after resets
- remember durable user context
- update that context over time
- distinguish between general questions and personal facts

## Recommended layered model

### 1. Canonical storage
Human-readable source of truth.
Examples:
- markdown vault
- plain text files
- structured JSON/YAML docs
- database-backed note system with exportable records

### 2. Retrieval indexes
Built from canonical storage.
Examples:
- SQLite FTS
- Postgres full-text search
- Elasticsearch / OpenSearch
- FAISS / pgvector / Qdrant / Weaviate / Pinecone

### 3. Operational memory
Small local layer for:
- startup behavior
- recent captures
- compatibility summaries
- pointers to the canonical store

## Flexibility principle
Do not hardcode one deployment model.
The user may choose:
- same-device embeddings
- separate-device embeddings
- cloud embeddings
- local-only operation
- hybrid local/cloud operation

The architecture should explain trade-offs, not force one answer.
