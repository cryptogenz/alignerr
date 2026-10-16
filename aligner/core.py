from pathlib import Path

SOURCE_SUFFIXES = {".py", ".js", ".ts", ".md"}
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}


def parse_requirements(text):
    """Return the bullet points from a Markdown requirements file."""
    items = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("-", "*")):
            items.append(stripped.lstrip("-* ").strip())
    return items


def read_repo(repo):
    """Concatenate all source files in the repo into one lowercase string."""
    chunks = []
    for path in Path(repo).rglob("*"):
        if not path.is_file() or path.suffix not in SOURCE_SUFFIXES:
            continue
        if SKIP_DIRS & set(path.parts):
            continue
        chunks.append(path.read_text(errors="ignore").lower())
    return "\n".join(chunks)


def check(requirements, repo):
    """Score each requirement as implemented, partial or missing."""
    corpus = read_repo(repo)
    results = {}
    for req in requirements:
        words = [w for w in req.lower().split() if len(w) > 3]
        hits = sum(1 for w in words if w in corpus)
        if words and hits == len(words):
            results[req] = "implemented"
        elif hits > 0:
            results[req] = "partial"
        else:
            results[req] = "missing"
    return results
