import sys
from scanner.scanner import scan_directory

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)

    path = sys.argv[1]
    results = scan_directory(path)

    if not results:
        print("✅ No keys found")
    else:
        for r in results:
            print(f"[!] {r[2]} found in {r[0]} at line {r[1]}")