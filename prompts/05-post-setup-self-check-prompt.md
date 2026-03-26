# Prompt 5 — Post-Setup Self-Check

## What this prompt is for
Use this prompt if you want the assistant to summarize whether the setup is ready before you trust it.

## Where to use it
Paste this prompt directly into the assistant chat in the OpenClaw UI.

## Prompt to paste into chat

```text
You are now in post-setup self-check mode.

Your job is to evaluate whether the knowledge-base system appears ready for normal use.
Do not continue the interview in this message.

Check these areas:
1. startup layer visibility
2. canonical KB path visibility
3. technical setup readiness
4. understanding of generic vs personal distinction
5. readiness to begin or continue foundational interviewing

Return your answer in this structure:
- Startup layer: OK / NOT OK
- KB path: OK / NOT OK
- Technical setup: OK / NOT OK
- Interview readiness: OK / NOT OK
- Main remaining issue: ...
- Suggested next step: ...

At the end of your message, include one of these:
STAGE COMPLETE: POST-SETUP SELF-CHECK
or
STAGE BLOCKED: POST-SETUP SELF-CHECK
```
