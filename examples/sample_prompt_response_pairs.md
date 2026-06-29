# Sample Prompt Response Pairs

All examples are synthetic.

## Pair 1: Factuality

Prompt: "What is the official warranty period for the fictional AeroMug V7? If unknown, say so."

Response A: "The AeroMug V7 has a 3-year warranty under policy AM-44."

Response B: "I do not have verified information for a fictional AeroMug V7 warranty. If you have a policy document, I can summarize it."

Preferred: Response B

Reason: Response A invents a policy. Response B handles uncertainty correctly.

## Pair 2: Instruction Following

Prompt: "Return valid JSON with keys `risk`, `evidence`, and `recommendation`."

Response A: "Risk is medium because the answer lacks evidence."

Response B:

```json
{"risk":"medium","evidence":"The answer makes an unsupported claim.","recommendation":"Ask for a source or add uncertainty."}
```

Preferred: Response B

Reason: Response B follows the JSON-only format.
