# Prompt Integration

This repository contains prompt files that are meant to be **copied and pasted into the assistant chat in stages**, unless your runtime gives you a better system-instruction integration path.

## Important principle
The prompt files are not magical by themselves.
A prompt only works if the assistant actually receives it.

So this repo supports two usage modes:

### Mode A — chat-driven setup (recommended for most users)
The user manually pastes the prompts into the assistant chat in order.
This is the easiest path for most people.

### Mode B — runtime/system integration
If your environment supports custom system prompts or assistant instruction files, you can integrate the same logic there.
In that case, the prompt files act as source material.

## Recommended default: chat-driven staged setup
Use the prompts in this order:

1. `prompts/01-startup-prompt.md`
2. `prompts/02-technical-setup-prompt.md`
3. `prompts/03-startup-validation-prompt.md`
4. `prompts/04-initial-interview-prompt.md`
5. optional: `prompts/05-post-setup-self-check-prompt.md`

## What each prompt does
### Prompt 1
Validates early startup visibility and KB activation intent.

### Prompt 2
Clarifies the user's technical situation and recommends a practical technical stack.

### Prompt 3
Validates startup behavior:
- reads workspace startup files
- reads `KB_CONFIG.md`
- confirms KB path visibility
- checks canonical-vs-operational memory understanding

### Prompt 4
Starts the real foundational interview.
This is the context-building stage.

### Prompt 5
Optional final readiness/self-check.
Use if you want the assistant to summarize whether the setup seems ready.

## Stage completion markers
Each prompt tells the assistant to end with a clearly labeled status line such as:
- `STAGE COMPLETE: ...`
- or `STAGE BLOCKED: ...`

This is intentional.
It lets the user know whether to continue to the next prompt or fix something first.

## Minimum rule
No matter how your runtime works, make sure these behaviors are actually enforced:
- startup files are read before substantive personal answering
- the canonical KB path is known
- retrieval happens before answering when personal context matters
- generic topic requests are not treated like personal facts
- reusable facts are saved instead of transcript dumps
- initial interview is offered when setup is ready and context is still sparse
