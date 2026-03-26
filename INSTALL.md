# Installation Guide

This guide assumes the assistant will run inside **OpenClaw**.

---

# Table of contents
1. Install OpenClaw
2. Connect a model
3. Start Gateway and open the UI
4. Finish OpenClaw base setup
5. Replace workspace startup files
6. Set the canonical KB path
7. Create the canonical knowledge base
8. Choose retrieval/indexing setup
9. Use prompts in chat
10. Run tests
11. Launch the initial interview
12. Maintain the system

---

## 1. Install OpenClaw
Run:

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

Then complete the normal first-run OpenClaw setup on the machine where the assistant will run.

---

## 2. Connect a model
Recommended baseline:
- model: any **GPT-5.x** model available in OpenClaw
- provider: **OpenAI Codex OAuth**

You can adapt this later if you want another provider/model, but this is the intended default path for this template.

---

## 3. Start Gateway and open the UI
Before using the staged prompts, open a terminal and run:

```bash
openclaw gateway run
```

Then open the chat UI in your browser:
- `http://127.0.0.1:18789`

Use that UI chat for the staged prompts.

---

## 4. Finish OpenClaw base setup first
Before adding the KB layer:
- make sure OpenClaw itself runs correctly
- let it create its normal default workspace files
- verify that the assistant can answer at all

Do not skip this.
The KB layer should be added **after** the runtime works.

---

## 5. Replace/adapt workspace startup files
After OpenClaw creates the default workspace files, open this repo's `workspace-template/` folder.

Copy/adapt these files into the real assistant workspace:
- `workspace-template/AGENTS.md`
- `workspace-template/STARTUP.md`
- `workspace-template/MEMORY.md`
- `workspace-template/KB_CONFIG.md`
- `workspace-template/memory/README.md`
- optional: `workspace-template/SOUL.md`
- optional: `workspace-template/USER.md`

### Merge vs replace rule
- if the generated OpenClaw file is only a generic placeholder, full replacement is usually fine
- if the generated file already contains user-specific material you want to keep, merge carefully instead of blindly overwriting

### Why
These files are the startup layer.
They make sure the assistant:
- re-enters the KB system after resets
- knows where canonical memory lives
- does not confuse local memory with the main KB
- retrieves before substantive personal answers
- offers a foundational interview when context is sparse

---

## 6. Set the canonical KB path
Open:
- `workspace-template/KB_CONFIG.md`

Replace:
- `REPLACE_THIS_WITH_THE_ACTUAL_ABSOLUTE_PATH_TO_YOUR_CANONICAL_KB`

with the real absolute path to your canonical knowledge base.

Examples:
- `/home/your-user/personal-kb`
- `/opt/personal-kb/vault`
- `/srv/assistant-memory/main-vault`

### Important rule
This file should become the startup-visible source of truth for where canonical memory lives.
If the path changes later, update `KB_CONFIG.md`.

---

## 7. Create the canonical knowledge base
Use `vault-template/` as the base.

Suggested top-level sections:
- `00-system/`
- `10-identity/`
- `20-preferences/`
- `30-projects/`
- `40-people/`
- `50-decisions/`
- `60-context/`
- `70-daily/`
- `80-summaries/`
- `90-archive/`

You may rename, expand, or simplify this structure.

### Important rule
The canonical KB is the durable source of truth.
Indexes are derived artifacts.
Do not treat the vector DB as the source of truth.

---

## 8. Choose retrieval/indexing setup
You can use any retrieval architecture you want.

### Valid options
- local-only
- split-device
- local + cloud embeddings
- managed vector DB
- hybrid retrieval

### Simplest starter path
If you want the minimum working setup, start with:
- canonical markdown notes
- keyword search only
- manual or scripted reindex after note changes

See:
- `scripts/minimal-retrieval-starter.md`

Examples of reference files in this repo:
- `schemas/sqlite_mock.sql`
- `schemas/metadata-example.json`
- `scripts/retrieve_context_example.py`
- `scripts/queue_reindex_example.py`
- `scripts/process_reindex_queue_example.py`
- `scripts/reindex_notes.sh`
- `scripts/embedding_options.md`

These are examples only.

---

## 9. Use prompts in chat
Open the files in `prompts/` and use them in this order inside the OpenClaw UI chat:

1. `prompts/01-startup-prompt.md`
2. `prompts/02-technical-setup-prompt.md`
3. `prompts/03-startup-validation-prompt.md`
4. `prompts/04-initial-interview-prompt.md`
5. optional: `prompts/05-post-setup-self-check-prompt.md`

For each prompt:
- open the file
- copy the block under `Prompt to paste into chat`
- paste it into the assistant chat
- wait for the `STAGE COMPLETE` line before moving on

Also read:
- `docs/prompt-integration.md`

### Important clarification
Prompt files in this repo are designed to be pasted into the chat as staged setup commands.
They can also be adapted into runtime/system instructions if your environment supports that better.

---

## 10. Run tests
After setup, run these behavioral tests.

### Test 1
Prompt:
```text
Tell me about castles in Germany
```
Expected:
- answer only
- no automatic personal-memory update

### Test 2
Prompt:
```text
I plan to go to Germany, tell me about castles there
```
Expected:
- personal-context aware answer
- retrieval if useful
- possible memory update for travel intent

### Test 3
Prompt:
```text
I care a lot about battery life in phones
```
Expected:
- reusable preference capture if not already known

### Test 4
Startup/path test
Verify manually that the assistant:
- reads workspace startup files
- reads `KB_CONFIG.md`
- can identify the canonical KB path

See also:
- `scripts/test-cases.md`
- `scripts/check_behavior.md`

If test 1 and test 2 behave the same way, the setup is wrong.

---

## 11. Launch the initial interview
If you have already used Prompt 4, the foundational interview should already be started.
If not, you can type:

```text
Let's start the foundational interview for the knowledge base.
```

The assistant should then begin structured context collection.

### Early interview priorities
- communication style
- current life context
- plans
- projects
- constraints
- decision rules
- tools/devices

---

## 12. Maintain the system
Ongoing rules:
- update existing notes before creating duplicates
- save reusable facts, not transcripts
- keep local workspace memory small
- reindex after meaningful changes
- inspect stale index entries after deletes/moves
- refresh summaries when needed

Helpful files:
- `docs/maintenance.md`
- `docs/update-workflow.md`
- `docs/retrieval-workflow.md`
- `docs/prompt-integration.md`
- `scripts/test-cases.md`

---

## Final note
The goal is not to build the biggest memory.
The goal is to build a memory system that:
- starts correctly
- knows where the KB is
- retrieves the right context
- updates cleanly
- survives resets
- does not mistake topic mentions for durable personal facts
