import argparse
from pathlib import Path

from aligner.core import check, parse_requirements


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="aligner",
        description="Check a requirements list against a codebase.",
    )
    parser.add_argument("spec", help="Markdown file with a bullet list of requirements")
    parser.add_argument("repo", help="Path to the repo to check")
    args = parser.parse_args(argv)

    requirements = parse_requirements(Path(args.spec).read_text())
    results = check(requirements, args.repo)

    for req, status in results.items():
        print(f"[{status.upper():11}] {req}")

    done = sum(1 for s in results.values() if s == "implemented")
    print(f"\n{done}/{len(results)} requirements implemented")


if __name__ == "__main__":
    main()
