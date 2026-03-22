import os
import re
from quazer.scanner.regex_rules import AWS_KEY, PRIVATE_KEY, GENERIC_API_KEY
from quazer.scanner.entropy import is_high_entropy

# File types to ignore
IGNORE_EXTENSIONS = ('.pyc', '.exe', '.dll', '.bin')

# Files to ignore
IGNORE_FILES = ['regex_rules.py']

# Folders to ignore
IGNORE_DIRS = ['__pycache__', '.git']


def scan_file(filepath):
    results = []

    # Skip unwanted file types
    if any(filepath.endswith(ext) for ext in IGNORE_EXTENSIONS):
        return results

    # Skip specific files
    if any(ignore in filepath for ignore in IGNORE_FILES):
        return results

    try:
        with open(filepath, 'r', errors='ignore') as f:
            for i, line in enumerate(f.readlines(), start=1):

                # 🔥 ENTROPY DETECTION (smarter)
                words = re.findall(r'[A-Za-z0-9+/=#@!$%^&*]{20,}', line)

                for word in words:
                    # Skip common false positives
                    if word.isdigit():
                        continue
                    if word.lower().startswith("http"):
                        continue
                    if len(set(word)) < 6:
                        continue

                    if is_high_entropy(word):
                        results.append((filepath, i, "High Entropy Secret"))

                # Skip obvious false positives
                if "PRIVATE_KEY =" in line:
                    continue

                # 🔐 AWS Key
                if re.search(AWS_KEY, line):
                    results.append((filepath, i, "AWS Key"))

                # 🔐 Private Key Block
                if re.search(PRIVATE_KEY, line):
                    results.append((filepath, i, "Private Key"))

                # 🔐 Generic API Key
                if re.search(GENERIC_API_KEY, line):
                    results.append((filepath, i, "Generic API Key"))

    except Exception:
        pass

    return results


def scan_directory(path):
    findings = []

    for root, dirs, files in os.walk(path):

        # Remove ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            filepath = os.path.join(root, file)

            file_results = scan_file(filepath)
            findings.extend(file_results)

    return findings