import sys
import os
from quazer.scanner.scanner import scan_directory


def install_hook():
    hook_path = ".git/hooks/pre-commit"

    script = """#!/bin/sh
quazer run
"""

    with open(hook_path, "w") as f:
        f.write(script)

    os.chmod(hook_path, 0o775)
    print("✅ Quazer hook installed")


def run_scan():
    results = scan_directory(".")

    if results:
        print("❌ Secrets detected! Commit blocked.\n")
        for file, line, issue in results:
            print(f"{issue} in {file}:{line}")
        sys.exit(1)
    else:
        print("✅ No secrets found")
        sys.exit(0)


# 👇 PASTE YOUR main() HERE
def main():
    if len(sys.argv) < 2:
        print("""
🚀 Quazer - Secret Leak Prevention

Usage:
  quazer init   → install git protection
  quazer run    → scan manually
""")
        return

    command = sys.argv[1]

    if command == "init":
        install_hook()
    elif command == "run":
        run_scan()


# 👇 IMPORTANT: keep this
if __name__ == "__main__":
    main()