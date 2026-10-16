# Aligner

Aligner checks a list of requirements against a codebase and reports which ones are **implemented**, **partial** or **missing**.

Built for the OmniRush hackathon, Agents & Automation track.

## The problem

Teams write requirements in a doc, then build, then lose track of what was actually delivered. Checking by hand is slow and easy to skip. Aligner automates that check and gives you a report you can act on.

## How it works

1. You write requirements as a Markdown bullet list (see `examples/spec.md`).
2. Aligner scans the source files in a repo (`.py`, `.js`, `.ts`, `.md`).
3. Each requirement is scored by how many of its key terms appear in the code.
4. You get a report: implemented, partial or missing.

## Current status

- Working: spec parsing, repo scanning, keyword-based scoring, CLI, tests, Docker.
- Planned: an LLM agent layer that reads the matching code and judges each requirement properly, instead of keyword matching.

## Requirements

- Python 3.12 (pinned in `.python-version`)
- Docker (optional)

## Setup

```bash
git clone <your-repo-url>
cd aligner
python -m venv .venv
source .venv/bin/activate        # Windows Git Bash: source .venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env             # fill in values if you enable the agent layer
```

## Run

```bash
python -m aligner examples/spec.md .
```

Arguments: the requirements file, then the repo path to check.

## Test

```bash
pytest
```

## Docker

```bash
docker build -t aligner .
docker run --rm aligner --help
docker run --rm -v "$PWD":/work aligner /work/examples/spec.md /work
```

## Configuration

Settings live in environment variables. Copy `.env.example` to `.env` and fill it in. No secrets are committed to the repo.

## Project layout

```
aligner/        source code (core.py logic, cli.py entry point)
tests/          pytest tests
examples/       sample requirements file
Dockerfile      container build
```

## Built with OmniRush

- Session 1: project setup, README, Docker, tests, baseline checker.
- Session 2: (fill in)
- Session 3: (fill in)
- Session 4: (fill in)
