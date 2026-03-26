# Prompt 3 — Startup / Knowledge-Base Activation

## What this prompt is for
Use this prompt after the technical setup direction has been chosen.

## Where to use it
Paste this prompt directly into the assistant chat in the OpenClaw UI.

## What this prompt should achieve
This prompt tells the assistant to:
- read the workspace startup files
- read `KB_CONFIG.md`
- identify the canonical knowledge base path
- treat the canonical KB as the source of truth
- explain whether the startup layer is correctly visible
- stop after this startup-validation stage is complete

## Prompt to paste into chat

```text
You are now in startup-validation mode.

Your job in this stage is only to validate and activate the knowledge-base startup layer.
Do not begin the user interview yet.
Do not start broad memory collection yet.

Tasks:
1. Read the workspace startup files available in the workspace.
2. Read `KB_CONFIG.md`.
3. Identify the canonical knowledge base path from that file.
4. Verify that you understand the difference between:
   - canonical knowledge base
   - workspace operational memory
   - temporary local memory
5. Explain briefly whether the setup for startup behavior looks correct.
6. If something important is missing or ambiguous, say exactly what is missing.
7. If startup behavior looks correct, say that this startup-validation stage is complete.

Important behavior rules:
- Do not invent the KB path if `KB_CONFIG.md` exists.
- Do not treat workspace memory as the canonical biography when a canonical KB is configured.
- Do not begin the foundational interview in this stage.
- Keep the reply practical and brief.

At the end of your message, include a clearly labeled line:
STAGE COMPLETE: STARTUP VALIDATION

If the stage is blocked, instead include:
STAGE BLOCKED: STARTUP VALIDATION
and explain what the user must fix before continuing.
```
