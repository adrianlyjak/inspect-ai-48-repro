set up

```bash
git clone https://github.com/adrianlyjak/inspect-ai-48-repro
cd inspect-ai-48-repro
uv sync
```

run pytest, relative import works

```bash
uv run pytest app/evals/test_foo.py
```

`test_foo` runs successfully

execute

```bash
uv run inspect eval app/evals/eval_foo.py --model openai/gpt-4o-mini
```

bang!

```
...
    from ..prompts.foo import GREET
ImportError: attempted relative import beyond top-level package
```
