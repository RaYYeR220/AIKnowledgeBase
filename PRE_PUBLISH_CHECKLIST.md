# Pre-Publish Checklist

Use this checklist before uploading the template to GitHub.

## Repository sanity
- [ ] `README.md` explains what the project is and gives a practical setup path
- [ ] `INSTALL.md` contains a clear step-by-step setup path
- [ ] `QUICKSTART.md` gives a short minimal setup path
- [ ] license is present
- [ ] `.gitignore` exists
- [ ] empty template folders are preserved with `.gitkeep` or equivalent

## OpenClaw flow
- [ ] OpenClaw installation step is present
- [ ] recommended model path is present (`gpt-5.x` + OpenAI Codex OAuth)
- [ ] docs tell the user to run `openclaw gateway run`
- [ ] docs tell the user to open `127.0.0.1:18789`
- [ ] docs make it clear that OpenClaw base setup should be completed first
- [ ] docs explain that generated default workspace files may need replacement/adaptation

## Workspace startup layer
- [ ] `workspace-template/AGENTS.md` exists
- [ ] `workspace-template/STARTUP.md` exists
- [ ] `workspace-template/MEMORY.md` exists
- [ ] `workspace-template/KB_CONFIG.md` exists
- [ ] workspace files clearly state that canonical KB is the source of truth
- [ ] workspace files clearly state that local memory is operational, not canonical
- [ ] startup layer tells the assistant to retrieve before substantive personal answers
- [ ] startup layer tells the assistant to read `KB_CONFIG.md`
- [ ] startup layer tells the assistant to offer an initial interview after technical setup if context is sparse

## Canonical KB layer
- [ ] `vault-template/` exists
- [ ] it includes system/rules notes
- [ ] it includes identity/preferences/projects/context/daily/summaries sections
- [ ] docs make it clear that indexes are derived artifacts, not source of truth

## Prompt flow
- [ ] prompts are designed for copy-paste into the chat
- [ ] each prompt explains what it is for
- [ ] each prompt tells the user where to use it
- [ ] each prompt contains a `Prompt to paste into chat` block
- [ ] each stage tells the assistant to emit `STAGE COMPLETE` or `STAGE BLOCKED` when appropriate
- [ ] docs explain the order in which prompts should be used

## Behavioral rules
- [ ] generic vs personal distinction is documented
- [ ] saving reusable facts instead of transcript dumps is documented
- [ ] operational memory compression is documented
- [ ] update-existing-first behavior is documented
- [ ] stale-index warning/maintenance is documented somewhere

## Technical flexibility
- [ ] docs do not force one storage backend unnecessarily
- [ ] docs do not force one embedding topology unnecessarily
- [ ] local / split-device / cloud / hybrid options are mentioned
- [ ] there is at least one minimal starter path for less technical users

## Initial interview
- [ ] there is a dedicated prompt for the first interview
- [ ] docs explain that technical setup alone is not enough without context population

## Tests
- [ ] test case for generic query exists
- [ ] test case for personal query exists
- [ ] docs explain that those two cases should not be treated the same
- [ ] there is a startup/path behavior check

## Privacy / cleanliness
- [ ] no personal user data from the original system is present
- [ ] no secrets or local credentials are included
- [ ] no machine-specific private paths are presented as mandatory for all users
- [ ] example scripts are clearly marked as examples, not production guarantees

## Final human review
- [ ] skim the repo as if you are a new user
- [ ] check whether the setup order is obvious
- [ ] check whether the reason for the KB is obvious
- [ ] check whether startup behavior is emphasized enough
- [ ] check whether the KB path declaration is obvious enough
- [ ] check whether prompt usage is obvious enough
- [ ] check whether the project feels flexible rather than over-engineered
