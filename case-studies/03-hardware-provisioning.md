# Case Study 3: New-Hire Laptop Provisioning

> **SIMULATED SCENARIO.** The ticket, employee, asset tag, serial number, and checklist results are synthetic. They come from no real employer or inventory. I have not managed a real device fleet through this process.

## Ticket (synthetic)

| Field | Value |
|---|---|
| Ticket ID | SIM-0003 |
| Priority | P3 (start date in 3 business days) |
| Request | Provision one laptop for "Riley Example" (fictional), Help Desk Analyst, starting Monday |
| Assumed environment | Company-managed laptops, a central identity system, and an asset inventory. Specific tools vary and are not named here. |

## Provisioning workflow

1. **Approve and reserve.** Confirm the request has manager approval. Reserve a device from inventory.
2. **Record the asset.** Log the asset tag, serial number, model, assigned user, and status ("In provisioning") in the inventory. Example: tag `SIM-A-1042`, serial `SIMSERIAL000`.
3. **Update and image.** Install OS updates and apply the company's standard configuration.
4. **Apply the security baseline.**
   - Disk encryption on, and the recovery key escrowed in the approved location (never emailed or put in the ticket)
   - Firewall on
   - Endpoint protection installed and reporting
   - Automatic updates on
   - Standard user rights (no local admin unless approved)
5. **Create access.** Set up the user account and the approved apps and groups only. Access is based on the role, not on what the employee asks for.
6. **Test.** Sign in as the user, check Wi-Fi/VPN, email, and printing.
7. **Hand off.** Verify identity at pickup, collect a signed acknowledgment, update inventory to "Assigned," and deliver the password securely (never by plain email).

## Synthetic verification checklist

| Check | Result (synthetic) |
|---|---|
| Disk encryption enabled | Pass |
| Recovery key escrowed | Pass |
| Firewall enabled | Pass |
| Endpoint agent reporting | **Fail: agent not checking in** |
| OS fully patched | Pass |
| Admin rights removed | Pass |

**Decision:** I hold the device and don't ship it. I first re-run the agent enrollment. If it still isn't reporting, I escalate to the endpoint security team, and I note the delay in the ticket.

## Escalation boundaries

- Escalate when the security baseline can't be met, the device is missing from inventory, or a requested access level needs approval.
- Do not grant extra permissions, skip encryption, or bypass endpoint protection to meet a deadline.
- Hardware faults (won't boot, battery swelling) go to the warranty or repair process. Stop using a swollen battery.

## Customer-facing note (synthetic)

> Hi Riley, your laptop is being prepared for Monday. One security check needs another pass, so I'll confirm by Friday noon whether it's ready. On Monday, bring a photo ID for pickup. You'll get your sign-in details in person, not by email. Reply if you need anything else.

## Assumptions and limits

- Simulated process. The tools, policies, and inventory system are generic and assumed.
- Steps are vendor-neutral. Real environments use specific MDM and imaging tools that I have not used here.
