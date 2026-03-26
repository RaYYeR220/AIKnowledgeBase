# KB_CONFIG.md - Workspace Template

## Canonical Knowledge Base Location
Set the absolute path to your canonical knowledge base here.

Example:
- `/home/your-user/knowledge-base`
- `/opt/personal-kb/vault`
- `/srv/assistant-memory/main-vault`

## Required Rule
The assistant should treat the path written in this file as the startup-visible location of the canonical knowledge base.
If the canonical KB path changes, update this file.

## Expected Use
On cold start, the assistant should:
1. read this file
2. identify the canonical KB path
3. use that path when reading memory rules / indexes / summaries / notes

## Your KB Path
- REPLACE_THIS_WITH_THE_ACTUAL_ABSOLUTE_PATH_TO_YOUR_CANONICAL_KB
