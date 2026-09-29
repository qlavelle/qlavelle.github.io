# Case Study 1: Account Lockout and Password Reset

> **SIMULATED SCENARIO.** The ticket, user, host names, and logs below are synthetic. I wrote them to practice. They come from no real employer, customer, or system. The domain `example.local` and the IP range `192.0.2.0/24` are reserved for documentation. The log format follows Windows Security event conventions.

## Ticket (synthetic)

| Field | Value |
|---|---|
| Ticket ID | SIM-0001 |
| Priority | P3 (single user, workaround exists) |
| Reported by | "Jordan Sample" (fictional) |
| Summary | "I can't log in. It says my account is locked." |
| Environment (assumed) | Windows domain `example.local`, remote staff on VPN |

## Sanitized synthetic log excerpt

```text
2026-01-12 08:41:02 EventID=4625 Account=jsample Status=0xC000006A (bad password) LogonType=3 Source=192.0.2.44
2026-01-12 08:41:19 EventID=4625 Account=jsample Status=0xC000006A (bad password) LogonType=3 Source=192.0.2.44
2026-01-12 08:41:33 EventID=4625 Account=jsample Status=0xC000006A (bad password) LogonType=3 Source=192.0.2.44
2026-01-12 08:41:34 EventID=4740 Account=jsample Locked out (caller: DC-SIM01)
```

## Troubleshooting decisions

1. **Verify identity first.** I follow the (assumed) policy: confirm two identifiers on a call-back to the number on file. A resettable password is a target for social engineering.
2. **Read the evidence.** Three bad-password events came from a single source, then a lockout. That fits a mistyped or stale saved password, not a distributed attack.
3. **Find the source.** `192.0.2.44` maps to the user's laptop. The user says a phone still has the old password saved for email or Wi-Fi. That device is a likely cause of repeat lockouts.
4. **Unlock, then decide on a reset.** If the user remembers the password, I unlock only. If not, I reset with a temporary password and force a change at next sign-in.
5. **Prevent a repeat.** I ask the user to update the saved password on all devices.

## Escalation boundaries

Escalate to the security team and don't reset the password myself if:
- Failed attempts come from multiple unfamiliar sources or countries.
- The account is privileged (admin, finance, executive).
- The user reports a phishing email or sharing credentials.
- Lockouts keep recurring after the saved credentials are cleared.

Escalate to the identity or systems team for lockouts I can't trace, or for policy changes.

## Customer-facing note (synthetic)

> Hi Jordan, your account was locked after several incorrect password attempts. I confirmed your identity and unlocked it. Please sign in again. If a phone or tablet still has your old password saved, update it there too, or the account may lock again. If it locks again, reply to this ticket and I'll investigate further. Thanks!

## Assumptions and limits

- Tool names and menus vary by environment. This scenario assumes Active Directory, but the same decisions apply to other identity systems.
- I have not deployed this in production. The ticket and logs are invented.

## My hands-on verification (complete after doing the task)

_[Add what you personally did, the date, and screenshots.]_

## AI assistance

An AI assistant helped draft this write-up. I reviewed it against my own testing and Microsoft documentation.
