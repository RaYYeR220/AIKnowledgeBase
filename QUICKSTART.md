# Quickstart

If you want the shortest possible path, do this:

## 1. Install OpenClaw
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

## 2. Connect a model
Inside OpenClaw, connect:
- any GPT-5.x model
- provider: OpenAI Codex OAuth

## 3. Start Gateway and open the UI
In a terminal, run:

```bash
openclaw gateway run
```

Then open:
- `http://127.0.0.1:18789`

## 4. Finish base OpenClaw setup
Make sure OpenClaw works normally first.
Let it create its default workspace files.

## 5. Replace/adapt workspace files
Use:
- `workspace-template/AGENTS.md`
- `workspace-template/STARTUP.md`
- `workspace-template/MEMORY.md`
- `workspace-template/KB_CONFIG.md`
- `workspace-template/memory/README.md`

## 6. Set the KB path
Open `workspace-template/KB_CONFIG.md` and replace the placeholder with the real absolute path to your canonical knowledge base.

## 7. Create/adapt canonical KB
Start from `vault-template/`.

## 8. Use prompts in chat in this order
1. `prompts/01-startup-prompt.md` — preflight check
2. `prompts/02-technical-setup-prompt.md` — technical setup
3. `prompts/03-startup-validation-prompt.md` — startup validation
4. `prompts/04-initial-interview-prompt.md` — start the interview
5. optional: `prompts/05-post-setup-self-check-prompt.md` — final self-check

For each prompt:
- open the file
- copy the block under `Prompt to paste into chat`
- paste it into the OpenClaw UI chat
- wait for the `STAGE COMPLETE` line before moving on

## 9. If you want the easiest technical version, start simple
Use:
- canonical markdown notes
- keyword search only
- manual reindex or a simple script

See:
- `scripts/minimal-retrieval-starter.md`

## 10. Test behavior
Type these prompts:

```text
Tell me about castles in Germany
```

```text
I plan to go to Germany, tell me about castles there
```

```text
I care a lot about battery life in phones
```

If the first two are treated the same way, the setup is wrong.
