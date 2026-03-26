# Workspace Startup Guidelines

The biggest failure mode is not bad storage design — it is that the assistant never re-enters the knowledge system on session start.

## Therefore
The workspace should contain startup files that are read before substantive answering.

## Suggested startup files
- `AGENTS.md` or equivalent workspace instructions
- `STARTUP.md` for cold-start memory behavior
- `KB_CONFIG.md` for canonical KB path declaration
- `MEMORY.md` as compressed operational memory, not a full biography
- optional `SOUL.md` / `USER.md`

## What startup layer should enforce
- where canonical memory lives
- which notes explain retrieval and update behavior
- that local summaries are not canonical if a larger KB exists
- that topic-specific retrieval happens before personal answers
- that personal facts are saved differently from generic topic requests
- that after technical setup the assistant should offer a foundational interview if the KB is still sparse

## Path rule
Do not rely on the assistant to guess the canonical KB location.
Declare it explicitly in `KB_CONFIG.md`.

## OpenClaw-specific recommendation
Let OpenClaw create its default workspace first.
Then replace/adapt the generated workspace files using the templates from this repository if you need different startup/memory behavior.
