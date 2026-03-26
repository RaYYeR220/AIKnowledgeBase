# Embedding Options

You do not need to force one embedding topology.

Valid options include:
- same-machine embeddings
- another local device with more GPU/CPU resources
- a local network service
- a cloud embedding API
- batched offline embedding jobs

## Decision factors
- privacy
- latency
- hardware availability
- operating cost
- reliability
- complexity of orchestration

## Recommendation
Design the retrieval layer so embedding generation is a replaceable component, not a hardcoded assumption.
