# Manual Behavior Check

After setup, verify these behaviors manually:

## Startup
- the assistant reads workspace startup files
- the assistant reads `KB_CONFIG.md`
- the assistant can identify the canonical KB path

## Retrieval
- generic queries do not automatically trigger deep personal memory usage unless useful
- personal queries do retrieve relevant user context when useful

## Saving
- generic topic requests are not saved as personal facts
- stable preferences/plans/constraints are saved as reusable facts

## Interview
- when technical setup is done but memory is sparse, the assistant offers a foundational interview
