# Case Study 2: "The Internet Is Down" (DNS vs. IP Troubleshooting)

> **SIMULATED SCENARIO.** The ticket, hostnames, and command output are synthetic, written for practice. Addresses use `192.0.2.0/24` and `example.local`, ranges reserved for documentation. Output is formatted like Windows tools but was not captured from a real network.

## Ticket (synthetic)

| Field | Value |
|---|---|
| Ticket ID | SIM-0002 |
| Priority | P3 (one user; P2 if several users report it) |
| Summary | "Websites won't load. Teams still works." |
| Environment (assumed) | Windows laptop, office Wi-Fi, DHCP, internal DNS server at 192.0.2.53 |

## Troubleshooting flow

I test from the bottom up, one layer at a time:

1. **Physical/Wi-Fi:** Is the laptop connected? Is the signal good?
2. **IP configuration:** `ipconfig /all`
3. **Local network:** `ping 192.0.2.1` (the gateway)
4. **Outside network by IP:** `ping 198.51.100.10` (a documentation address standing in for an external host)
5. **DNS:** `nslookup example.com`

## Synthetic output and interpretation

```text
> ipconfig /all
   IPv4 Address. . . . . . . . . . . : 192.0.2.87
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.0.2.1
   DHCP Server . . . . . . . . . . . : 192.0.2.2
   DNS Servers . . . . . . . . . . . : 192.0.2.53

> ping 192.0.2.1
Reply from 192.0.2.1: bytes=32 time=2ms TTL=64

> ping 198.51.100.10
Reply from 198.51.100.10: bytes=32 time=18ms TTL=54

> nslookup example.com
DNS request timed out.
    timeout was 2 seconds.
*** Request to UnKnown timed out
```

**Reading it:** The laptop has a valid IP, reaches the gateway, and reaches an outside host by IP. Only name lookups fail, so this is a DNS problem, not a general connectivity problem. That also explains why Teams works: it may already hold cached connections or IPs.

## Decision table

| Symptom | Likely cause | First action |
|---|---|---|
| IP starts with 169.254.x.x | DHCP failed (APIPA address) | Reconnect, then `ipconfig /release` and `ipconfig /renew` |
| Can't ping gateway | Local link or Wi-Fi issue | Check connection, try another port or AP |
| Ping by IP works, names fail | DNS issue | Check DNS server setting, `ipconfig /flushdns`, test another DNS server |
| Names work on one device, not another | Device-specific config or cache | Compare settings, flush cache |

## Actions taken (simulated)

1. Ran `ipconfig /flushdns`. The lookup still failed.
2. Ran `nslookup example.com 192.0.2.54` (a second internal DNS server, assumed to exist). It answered, so the first DNS server is likely the problem.
3. Asked another user to run the same lookup. It failed for them too, so this is not just one laptop. **I raised the ticket to P2.**

## Escalation boundaries

- **Escalate to network/infrastructure:** the DNS server is unresponsive for multiple users, or DHCP hands out wrong DNS settings.
- **Do not:** change DNS server configuration, DHCP scopes, or firewall rules without authorization.
- **Temporary workaround** (only if policy allows): a manual alternate internal DNS server. Never point a work device at an unapproved public resolver.

## Customer-facing note (synthetic)

> Hi, we found that the issue is with the name-lookup service (DNS), which affects several users, not just your computer. I've escalated it to the network team. Teams and other apps that are already connected may keep working. I'll update you within one hour or as soon as it's fixed.

## Assumptions and limits

- Simulated environment. I have not deployed or repaired a real DNS server.
- Commands are Windows-specific. macOS and Linux use different tools (`scutil --dns`, `dig`, `resolvectl`).

## My hands-on verification

_[Add what you personally ran on your own devices and networks, with sanitized screenshots.]_

## AI assistance

An AI assistant helped draft this case study. I reviewed the commands against Microsoft documentation and my own testing.
