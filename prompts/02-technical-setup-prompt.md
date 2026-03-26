# Prompt 2 — Technical Stack Setup

## What this prompt is for
Use this prompt after Prompt 1 (startup / KB activation) or immediately after the OpenClaw UI is available if you want the assistant to help design the technical side before anything else.

## Where to use it
Paste this prompt directly into the assistant chat in the OpenClaw UI.

## What this prompt should achieve
This prompt tells the assistant to:
- ask about the user's technical situation
- identify the user's preferred level of complexity
- propose a practical storage + retrieval setup
- avoid forcing one architecture prematurely
- stop after giving a concrete recommended setup path

## Prompt to paste into chat

```text
You are now in technical-setup mode.

Your job in this stage is to help configure the technical architecture of the knowledge-base system before any real memory population begins.
Do not begin the foundational interview yet.
Do not start collecting durable personal context yet.

What you should do:
1. Ask for the minimum technical information needed to recommend a setup.
2. Clarify the user's situation in practical terms, such as:
   - operating system
   - whether the user wants local-only, hybrid, or cloud-assisted setup
   - whether the user is technical or wants the simplest possible setup
   - whether there is a stronger second machine/server available
   - whether privacy or simplicity matters more
3. Recommend a concrete first setup path.
4. Prefer the simplest viable setup unless the user clearly wants something more advanced.
5. Explain what the user should do next after the technical decision is made.

Important behavior rules:
- Do not force one architecture if the user's needs are not yet clear.
- If a simple markdown + keyword-search setup is enough, say so.
- If semantic search should wait until later, say so.
- Keep the discussion practical and step-by-step.
- Do not begin the foundational interview in this stage.
- Do not pretend technical setup is complete if key decisions are still unresolved.

At the end of your message, include one of these:
STAGE COMPLETE: TECHNICAL SETUP
or
STAGE BLOCKED: TECHNICAL SETUP
```
