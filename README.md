# Code Reviewer CLI

A small Python command-line code reviewer built for the hackathon prompt. It parses files with Python's `ast` module, reports line numbers, and can optionally ask Groq or Gemini for a plain-language explanation and a suggested code snippet. It uses **only the Python standard library**.

## Run it

```bash
python reviewer.py sample.py
```

Try the folder scanner and a saved report:

```bash
python reviewer.py . --report review.md
```

For JSON output:

```bash
python reviewer.py sample.py --format json --report review.json
```

## Optional LLM explanations

Set one API key in your shell. The key is read from the environment and is never saved by this program.

**Groq (bash/macOS/Linux):**

```bash
export GROQ_API_KEY="your_key"
python reviewer.py sample.py --provider groq --show-code
```

**Gemini (bash/macOS/Linux):**

```bash
export GEMINI_API_KEY="your_key"
python reviewer.py sample.py --provider gemini --show-code
```

PowerShell example: `$env:GROQ_API_KEY="your_key"` (or `$env:GEMINI_API_KEY="your_key"`). You can set `GROQ_MODEL` or `GEMINI_MODEL` to override the default model, or pass `--model MODEL_NAME`.

Without a key, the tool still runs offline and prints the static finding and a basic fix suggestion. To explicitly keep everything offline, use `--provider none`. If an LLM is enabled, a short code excerpt around each finding is sent to that provider. The tool does not execute model output or modify the reviewed file. `--show-code` only displays the proposed snippet.

## Checks included

- Missing docstrings on public functions, async functions, and classes.
- Deep control-flow nesting (default threshold: 4; change with `--max-nesting 3`).
- Assigned-but-never-read local variables in functions (parameters and underscore-prefixed names are ignored).
- Unused imports.
- Mutable list/dict/set defaults.
- Bare or overly broad `except` handlers.

Folders are scanned recursively for `.py` files. Common environment/build folders and hidden folders are skipped.

Severity is assigned by the static checks. The score is a deliberately simple heuristic: start at 100 and subtract 15 for each high, 8 for each medium, and 3 for each low finding. Treat it as a demo summary, not a measure of correctness. The unused-variable/import checks are lightweight heuristics and can have false positives/negatives; run tests and use human review too.

## Hackathon demo flow

1. Run `python reviewer.py sample.py` to show AST parsing and multiple real findings.
2. Explain that each finding has a source line, severity, plain-language reason, and fix.
3. If you have a key, set it and run with `--show-code` to demonstrate LLM enrichment. Otherwise point out the offline fallback.
4. Run `python reviewer.py . --report review.md` to demonstrate folder review and report generation.
