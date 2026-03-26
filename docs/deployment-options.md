# Deployment Options

This system should allow multiple technical setups.

## Option A — fully local on one machine
Pros:
- simple mental model
- private
- low latency
Cons:
- local resource limits
- harder on weaker hardware

## Option B — split local architecture
Examples:
- canonical notes on one machine
- embeddings on another device with GPU
- retrieval orchestrator somewhere else on local network

Pros:
- better hardware utilization
- flexible scaling
Cons:
- more moving parts

## Option C — cloud-assisted retrieval/embeddings
Examples:
- cloud embeddings API
- managed vector DB
- cloud reranking service

Pros:
- easiest scaling
- lower local hardware needs
Cons:
- privacy and cost trade-offs
- network dependency

## Option D — hybrid
Canonical notes local, selective indexing or heavy inference elsewhere.

## Recommendation philosophy
The framework should present trade-offs and safe defaults, not lock the user into one topology.
