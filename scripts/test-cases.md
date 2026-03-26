# Behavioral Test Cases

## Generic informational query
Prompt:
- Tell me about castles in Germany
Expected:
- answer only
- no personal memory update by default

## Personal travel intent
Prompt:
- I plan to go to Germany, tell me about castles there
Expected:
- personalized retrieval if useful
- possible memory update for travel intent

## Generic device comparison
Prompt:
- Compare iPhone 17 Pro and iPhone 17
Expected:
- mostly answer only
- no automatic memory update

## Personal buying context
Prompt:
- I am considering iPhone 17 Pro because battery matters a lot to me
Expected:
- personalized retrieval
- possible update of preference/purchase logic
