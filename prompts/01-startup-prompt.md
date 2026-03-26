# Prompt 1 — Preflight / Workspace Visibility Check

## What this prompt is for
Use this prompt first, after:
- OpenClaw is installed
- the model is connected
- `openclaw gateway run` is active
- the UI is open at `http://127.0.0.1:18789`
- workspace template files were copied/adapted
- `KB_CONFIG.md` was filled with the real canonical KB path

## Where to use it
Paste this prompt directly into the assistant chat in the OpenClaw UI.

## What this prompt should achieve
This prompt tells the assistant to:
- confirm that the startup layer is visible
- confirm that `KB_CONFIG.md` exists and can be read
- confirm that a canonical KB path is declared
- report any obvious missing setup piece before deeper validation begins

## Prompt to paste into chat

```text
You are now in preflight-check mode.

Your job in this stage is to perform a minimal preflight check before deeper setup work begins.
Do not begin the foundational interview yet.
Do not start broad memory collection yet.
Do not do full startup validation yet.

Tasks:
1. Check whether the workspace startup files are visible.
2. Check whether `KB_CONFIG.md` is visible.
3. Check whether `KB_CONFIG.md` contains a declared canonical KB path.
4. Briefly report whether the setup appears ready for the next stage.
5. If something essential is missing, say exactly what is missing.

Important behavior rules:
- Keep the reply short and practical.
- Do not pretend setup is ready if `KB_CONFIG.md` is missing or still contains a placeholder path.
- Do not begin technical architecture questioning yet.
- Do not begin the foundational interview yet.

At the end of your message, include one of these:
STAGE COMPLETE: PREFLIGHT CHECK
or
STAGE BLOCKED: PREFLIGHT CHECK
```
