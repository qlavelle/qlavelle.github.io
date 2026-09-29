"""Simple log parser (beginner version).

Reads a text log, counts failed logins per source IP, and flags any
source that reaches a threshold. Works only on the SYNTHETIC format
shown in sample_auth.log.
"""
import argparse
import re
import sys
from collections import Counter

LINE_PATTERN = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<event>[A-Z_]+) user=(?P<user>\S+) src=(?P<src>\S+)$"
)


def parse_log(path):
    """Return (failed_by_src, users_by_src, lockouts, bad_lines)."""
    failed_by_src = Counter()
    users_by_src = {}
    lockouts = []
    bad_lines = 0

    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            match = LINE_PATTERN.match(line)
            if not match:
                bad_lines += 1
                continue
            event, user, src = match["event"], match["user"], match["src"]
            if event == "FAILED_LOGIN":
                failed_by_src[src] += 1
                users_by_src.setdefault(src, set()).add(user)
            elif event == "ACCOUNT_LOCKED":
                lockouts.append(user)
    return failed_by_src, users_by_src, lockouts, bad_lines


def main():
    parser = argparse.ArgumentParser(description="Flag sources with many failed logins.")
    parser.add_argument("logfile", help="path to the log file")
    parser.add_argument("--threshold", type=int, default=3,
                        help="failed logins needed to flag a source (default 3)")
    args = parser.parse_args()

    if args.threshold < 1:
        print("Error: --threshold must be 1 or higher.")
        return 1

    try:
        failed, users, lockouts, bad = parse_log(args.logfile)
    except FileNotFoundError:
        print(f"Error: file not found: {args.logfile}")
        return 1
    except PermissionError:
        print(f"Error: no permission to read: {args.logfile}")
        return 1
    except UnicodeDecodeError:
        print("Error: file is not readable text (UTF-8).")
        return 1

    print(f"Failed logins by source (threshold {args.threshold}):")
    if not failed:
        print("  none found")
    for src, count in failed.most_common():
        flag = "FLAG" if count >= args.threshold else "ok"
        names = ", ".join(sorted(users[src]))
        print(f"  {src}: {count} failed [{flag}] users tried: {names}")

    print(f"Account lockouts: {', '.join(lockouts) if lockouts else 'none'}")
    print(f"Malformed lines skipped: {bad}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
