# Monitoring Your Rollout

Track progress from the day installation begins. Regular monitoring catches blockers early and gives the Giga team the information needed to support you.

---

## Rollout health metrics

Three numbers to track from the start:

| Metric | Formula | What it tells you |
|---|---|---|
| **% schools installed** | Schools with Giga Meter ÷ target schools × 100 | Are you on pace with the deployment plan? |
| **% installed schools reporting** | Schools that sent data in the last 7 days ÷ installed schools × 100 | Are installed schools actually collecting data? |
| **Open troubleshooting tickets** | Count of unresolved support requests per week | Is the support mechanism keeping up with issues? |

> [!TIP]
> A school can be "installed" but not "reporting" — the device may be powered off, the app may have crashed, or it may have lost internet. Treat any installed school that hasn't reported in 7+ days as a priority follow-up.

---

## Reporting to Giga

- **First 3 months:** share a progress update every month — % installed, % reporting, open blockers, and anything that deviated from the plan.
- **After 3 months:** quarterly updates.

Updates can be as short as a one-paragraph email or a shared tracker. The goal is to keep the Giga team informed so they can support you.

---

## Dashboard: Installation Tracking screen

Once schools start reporting, use the **Installation Tracking** tab in the Superset dashboard to monitor rollout health in real time.

Key metrics on that screen:

| Dashboard figure | What it means |
|---|---|
| **Live schools** | Schools that sent a measurement in the last 21 days |
| **Drop-off** | Schools silent for 28+ days — unlikely to return without a site visit |
| **At-risk schools** | Schools in the 21–28-day quiet window — follow up before they drop off |
| **Drop-off rate** | Drop-offs ÷ total installed, as a percentage |

See [Using the Dashboard](../data/dashboard-guide.md) for a full walkthrough of the Installation Tracking screen.

---

## Escalation path

Between the school and the Giga team, there should be a government support layer:

```
School focal point
    ↓ (basic troubleshooting)
Installation lead / MoE IT department
    ↓ (unresolved issues)
Giga team (via UNICEF country office)
```

When escalating to Giga, include:
- School name and ID
- Giga Meter version installed (visible in the app's Settings)
- A screenshot or exact text of any error message
- What was tried before escalating

---

## Common post-installation issues

| Symptom | First step |
|---|---|
| School installed but not reporting | Check the device is powered on and connected during school hours (8 AM–8 PM) |
| School appears "Unknown" on Giga Maps | The school ID may not match Giga's records — verify the ID and contact the Giga team |
| App shows an error on launch | See [Troubleshooting](../troubleshooting/troubleshooting.md) |
| Whole district drops off at once | Could be a regional ISP outage — check with the ISP before escalating to Giga |

---

## Related pages

- [Government Onboarding Overview](government-onboarding-overview.md)
- [Deployment Checklist](deployment-checklist.md)
- [Using the Dashboard](../data/dashboard-guide.md)
- [Troubleshooting](../troubleshooting/troubleshooting.md)
