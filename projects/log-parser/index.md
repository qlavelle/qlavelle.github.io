# Failed-Login Log Parser (Python)

> **SYNTHETIC DATA.** `sample_auth.log` is invented for practice. It comes from no real system, employer, or customer. The tool is a learning project, not a production security tool.

## What it does

Reads a text log, counts failed logins per source IP, flags sources at or above a threshold, lists account lockouts, and counts lines it couldn't parse.

## Run it (free, Python 3 only)

```bash
python3 log_parser.py sample_auth.log
python3 log_parser.py sample_auth.log --threshold 5
```

## Expected output (default threshold of 3)

```text
Failed logins by source (threshold 3):
  198.51.100.7: 5 failed [FLAG] users tried: admin, guest, root, test
  192.0.2.44: 3 failed [FLAG] users tried: jsample
  192.0.2.51: 1 failed [ok] users tried: rexample
Account lockouts: jsample
Malformed lines skipped: 1
```

## How it works

1. Opens the file and reads it line by line.
2. Skips blank lines and `#` comments.
3. Matches each line against a regular expression for `date time EVENT user=... src=...`.
4. Counts `FAILED_LOGIN` events per source with a `Counter`, and records users tried per source.
5. Notes `ACCOUNT_LOCKED` events and counts lines that don't match.

## Error handling

- Missing file: prints an error and exits.
- No read permission or non-text file: prints an error and exits.
- Threshold below 1: prints an error and exits.
- Malformed lines: counted and skipped, not fatal.

## Limits

- Handles only this one synthetic format. Real logs (Linux auth, Windows events, firewall) need different parsing.
- Counts only totals. It ignores timing, so it can't tell a brute-force burst from failures spread over days.
- Not tested against real-world log data.
