import os
import re
from quazer.scanner.regex_rules import AWS_KEY, PRIVATE_KEY, GENERIC_API_KEY
from quazer.scanner.entropy import is_high_entropy
from quazer.scanner.regex_rules import STRUCTURED_KEY

IGNORE_EXTENSIONS = ('.pyc', '.exe', '.dll', '.bin')
IGNORE_FILES = ['regex_rules.py']
IGNORE_DIRS = ['__pycache__', '.git']

def scan_file(filepath):
    results = []
    if any(filepath.endswith(ext) for ext in IGNORE_EXTENSIONS):
        return results
    if any(ignore in filepath for ignore in IGNORE_FILES):
        return results

    try:
        with open(filepath, 'r', errors='ignore') as f:
            for i, line in enumerate(f.readlines(), start=1):
                words = re.findall(r'[A-Za-z0-9+/=#@!$%^&*]{20,}', line)
                for word in words:
                    if word.isdigit(): continue
                    if word.lower().startswith("http"): continue
                    if len(set(word)) < 6: continue
                    if is_high_entropy(word):
                        results.append((filepath, i, "High Entropy Secret"))

                # AWS / Private / Generic keys
                if re.search(AWS_KEY, line):
                    results.append((filepath, i, "AWS Key"))
                if re.search(PRIVATE_KEY, line):
                    results.append((filepath, i, "Private Key"))
                if re.search(GENERIC_API_KEY, line):
                    results.append((filepath, i, "Generic API Key"))

    except Exception:
        pass

    return results

def scan_directory(path):
    findings = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            filepath = os.path.join(root, file)
            findings.extend(scan_file(filepath))
    return findings