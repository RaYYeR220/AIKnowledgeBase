# OpenClaw Personal Knowledge Base Template

Use this repo if you want an OpenClaw assistant that:
- survives session resets
- retrieves personal context before answering when needed
- does not confuse generic topic questions with facts about the user
- can gradually build a durable knowledge base through structured interviews and normal conversation

---

# Start here: exact setup steps

This section is the main guide.
If you just want to install and run the system, follow these steps in order.

## 1) Install OpenClaw
Run:

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

Then complete the normal OpenClaw first-run flow.

---

## 2) Connect a model
Inside OpenClaw, connect:
- any **GPT-5.x** model
- provider: **OpenAI Codex OAuth**

Recommended baseline for this template:
- OpenClaw runtime
- OpenAI Codex OAuth provider
- GPT-5.x model

---

## 3) Start the OpenClaw Gateway UI
Before using the setup prompts, open a terminal and run:

```bash
openclaw gateway run
```

Then open the chat UI in your browser:

- `http://127.0.0.1:18789`

Use that UI chat for the staged prompts below.

---

## 4) Let OpenClaw create its default workspace files
Do **not** replace anything before OpenClaw has completed its normal setup.

The intended order is:
1. install OpenClaw
2. make sure the assistant starts normally
3. let the default workspace files appear
4. only then replace/adapt them using this repo

---

## 5) Replace/adapt the workspace startup files
Open the `workspace-template/` folder from this repo.

Copy/adapt these files into your real OpenClaw workspace:
- `workspace-template/AGENTS.md`
- `workspace-template/STARTUP.md`
- `workspace-template/MEMORY.md`
- `workspace-template/KB_CONFIG.md`
- `workspace-template/memory/README.md`
- optionally `workspace-template/SOUL.md`
- optionally `workspace-template/USER.md`

### Real workspace path
A common OpenClaw workspace path is:
- `/home/$USER/.openclaw/workspace`

If your installation uses another workspace path, use your actual OpenClaw workspace location instead.

### Merge vs replace rule
- if the generated OpenClaw file is only a generic placeholder, full replacement is usually fine
- if the generated file already contains user-specific material you want to keep, merge carefully instead of blindly overwriting

---

## 6) Set the canonical KB path
Open:
- `workspace-template/KB_CONFIG.md`

Replace:
- `REPLACE_THIS_WITH_THE_ACTUAL_ABSOLUTE_PATH_TO_YOUR_CANONICAL_KB`

with your real absolute KB path.

Examples:
- `/home/your-user/personal-kb`
- `/opt/personal-kb/vault`
- `/srv/assistant-memory/main-vault`

This file should become the startup-visible source of truth for where canonical memory lives.

---

## 7) Create your canonical knowledge base
Use `vault-template/` as a starting point.

You can:
- copy it directly
- modify it
- rename sections
- expand or shrink the structure

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

### Important rule
This canonical KB is the **source of truth**.
Your search indexes are not the source of truth.

---

## 8) Pick any retrieval/indexing architecture you want
This repo does **not** force one architecture.

You can use:
- local-only retrieval
- split-device retrieval
- cloud embeddings
- managed vector DB
- hybrid local/cloud setup

### Simplest starter path
If you want the minimum working setup, start with:
- canonical markdown notes
- keyword search only
- manual or scripted reindex after note changes

See:
- `scripts/minimal-retrieval-starter.md`

Reference files:
- `schemas/sqlite_mock.sql`
- `schemas/metadata-example.json`
- `scripts/retrieve_context_example.py`
- `scripts/queue_reindex_example.py`
- `scripts/process_reindex_queue_example.py`
- `scripts/reindex_notes.sh`
- `scripts/embedding_options.md`

These are examples, not production guarantees.

---

## 9) Use the setup prompts in chat
This repo supports a **chat-driven staged setup**.

Use the prompts in this order inside the OpenClaw UI chat at `http://127.0.0.1:18789`.

### Prompt 1 — preflight check
Open:
- `prompts/01-startup-prompt.md`

Copy the block under:
- `Prompt to paste into chat`

Paste it into the chat.

Wait for one of these lines:
- `STAGE COMPLETE: PREFLIGHT CHECK`
- `STAGE BLOCKED: PREFLIGHT CHECK`

Only continue when the stage is complete.

### Prompt 2 — technical setup
Open:
- `prompts/02-technical-setup-prompt.md`

Copy the block under:
- `Prompt to paste into chat`

Paste it into the chat.

Wait for one of these lines:
- `STAGE COMPLETE: TECHNICAL SETUP`
- `STAGE BLOCKED: TECHNICAL SETUP`

Only continue when the stage is complete.

### Prompt 3 — startup validation
Open:
- `prompts/03-startup-validation-prompt.md`

Copy the block under:
- `Prompt to paste into chat`

Paste it into the chat.

Wait for one of these lines:
- `STAGE COMPLETE: STARTUP VALIDATION`
- `STAGE BLOCKED: STARTUP VALIDATION`

Only continue when the stage is complete.

### Prompt 4 — foundational interview start
Open:
- `prompts/04-initial-interview-prompt.md`

Copy the block under:
- `Prompt to paste into chat`

Paste it into the chat.

Expected result:
- the assistant starts the foundational interview
- ends the kickoff with:
  - `STAGE COMPLETE: FOUNDATIONAL INTERVIEW STARTED`

### Optional Prompt 5 — self-check
Open:
- `prompts/05-post-setup-self-check-prompt.md`

Use this if you want a final readiness summary.

Also read:
- `docs/prompt-integration.md`

---

## 10) Run the first behavior tests
After setup, test these exact prompts:

### Test A
```text
Tell me about castles in Germany
```
Expected:
- normal informational answer
- no automatic personal-memory update

### Test B
```text
I plan to go to Germany, tell me about castles there
```
Expected:
- informational + personal handling
- retrieval of user context if useful
- possible memory capture of travel intent

### Test C
```text
I care a lot about battery life in phones
```
Expected:
- reusable preference capture if not already known

### Test D
Verify manually that the assistant:
- reads workspace startup files
- reads `KB_CONFIG.md`
- can identify the canonical KB path

See also:
- `scripts/test-cases.md`
- `scripts/check_behavior.md`

If the assistant treats Test A and Test B the same way, your setup is wrong.

---

## 11) Start and continue the foundational interview
Once Prompt 4 is used, the assistant should begin structured context collection.

What the interview should cover first:
- communication style
- current life context
- projects
- plans
- constraints
- decision rules
- important devices/tools

---

## 12) Keep the system clean over time
Main maintenance rules:
- update existing notes before creating duplicates
- save reusable facts, not transcripts
- keep local memory compressed
- reindex after meaningful changes
- check for stale index entries after deletes/moves
- refresh summaries occasionally

Helpful files:
- `docs/maintenance.md`
- `docs/update-workflow.md`
- `docs/retrieval-workflow.md`
- `docs/prompt-integration.md`
- `scripts/test-cases.md`

---

# What to open if you are setting this up
If you are doing the setup manually, open these files in this order:

1. `README.md`
2. `QUICKSTART.md`
3. `INSTALL.md`
4. `workspace-template/AGENTS.md`
5. `workspace-template/STARTUP.md`
6. `workspace-template/KB_CONFIG.md`
7. `prompts/01-startup-prompt.md`
8. `prompts/02-technical-setup-prompt.md`
9. `prompts/03-startup-validation-prompt.md`
10. `prompts/04-initial-interview-prompt.md`
11. optional: `prompts/05-post-setup-self-check-prompt.md`
12. `docs/prompt-integration.md`
13. `scripts/test-cases.md`

---

# What to copy into a real OpenClaw setup
## Copy/adapt into the workspace
- `workspace-template/AGENTS.md`
- `workspace-template/STARTUP.md`
- `workspace-template/MEMORY.md`
- `workspace-template/KB_CONFIG.md`
- `workspace-template/memory/README.md`
- optional: `workspace-template/SOUL.md`
- optional: `workspace-template/USER.md`

## Use as prompts to paste into chat
- `prompts/01-startup-prompt.md`
- `prompts/02-technical-setup-prompt.md`
- `prompts/03-startup-validation-prompt.md`
- `prompts/04-initial-interview-prompt.md`
- optional: `prompts/05-post-setup-self-check-prompt.md`

## Use as canonical KB starter
- everything inside `vault-template/`

---

# Why build a system like this?
Without a structured KB, assistants often:
- lose context after resets
- repeat onboarding questions
- answer too generically
- mix temporary details with durable user facts

A good KB gives the assistant a way to:
- re-anchor on cold start
- retrieve the right context when needed
- save reusable facts cleanly
- keep startup behavior predictable

---

# Core architecture
This template assumes 3 layers.

## 1. Canonical knowledge base
Durable source of truth.
Examples:
- markdown vault
- note tree
- structured text files

## 2. Retrieval layer
Built from the canonical KB.
Examples:
- SQLite FTS
- FAISS
- pgvector
- cloud vector DB
- hybrid retrieval stack

## 3. Operational workspace layer
Small startup/compatibility layer.
Examples:
- `AGENTS.md`
- `STARTUP.md`
- `MEMORY.md`
- `KB_CONFIG.md`
- recent local capture files

Important rule:
The operational layer should not become a second full biography.

---

# Generic vs personal queries
One of the key rules in this system:
- **generic topic request** != **personal fact**

Example:
- `Tell me about castles in Germany` -> answer only
- `I plan to go to Germany, tell me about castles there` -> answer + consider personalized retrieval + possible memory update

---

# Repository structure
```text
.
├── prompts/
├── docs/
├── schemas/
├── scripts/
├── workspace-template/
├── vault-template/
├── README.md
├── QUICKSTART.md
├── INSTALL.md
└── PRE_PUBLISH_CHECKLIST.md
```

---

# Recommended next files to read
- `QUICKSTART.md`
- `INSTALL.md`
- `docs/openclaw-specific-setup.md`
- `docs/workspace-startup-guidelines.md`
- `docs/prompt-integration.md`
- `scripts/test-cases.md`

---

# License
MIT — see `LICENSE.md`.
