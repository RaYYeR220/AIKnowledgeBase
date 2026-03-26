# OpenClaw-Specific Setup Notes

This template assumes a workflow where OpenClaw is the runtime host for the assistant.

## Recommended baseline
- install OpenClaw first
- connect a GPT-5.x model
- use OpenAI Codex OAuth as provider
- finish normal OpenClaw first-run setup
- only then replace/adapt workspace startup files and add the KB layer

## Why
The knowledge-base system should sit on top of a working assistant runtime.
If OpenClaw itself is not configured yet, KB startup behavior is harder to validate cleanly.

## Workspace rule
The generated default OpenClaw workspace files are only a starting point.
If their contents do not match the desired memory behavior, replace/adapt them with the versions in `workspace-template/`.

## KB path rule
The path to the canonical knowledge base should be declared in:
- `workspace-template/KB_CONFIG.md`

In a real setup, this file should be copied into the real workspace and updated with the actual absolute path.

## Important outcome
After setup, the assistant should:
- start from workspace startup files
- read `KB_CONFIG.md`
- identify the canonical KB path
- retrieve before substantive personal answers
- start a foundational interview when context is still sparse
