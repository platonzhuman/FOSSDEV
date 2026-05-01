import ast
import sys
from pathlib import Path

STD = {"sys","os","re","math","random","ast","pathlib","typing"}

def main():
    reqs = set()
    if Path("requirements.txt").exists():
        reqs = {line.strip().split("==")[0] for line in Path("requirements.txt").read_text().splitlines() if line.strip()}

    src_imports = set()
    for py_file in Path("src").rglob("*.py"):
        tree = ast.parse(py_file.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    src_imports.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                src_imports.add(node.module.split(".")[0])

    missing = src_imports - STD - reqs
    if missing:
        print("mising in requirements.txt:", ", ".join(missing))
        sys.exit(1)
    print("ALL IMPORT IS OK ^_^")

if __name__ == "__main__":
    main()