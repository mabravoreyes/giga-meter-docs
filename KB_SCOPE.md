# Giga Meter Knowledge Base — Full Scope Plan

> Synthesized from: ClickUp PRD (`rk10z-62337`), ClickUp Onboarding Process doc (`rk10z-63037`),  
> `GigaMeterFAQs.md`, Installation Strategy Template, v2.0.2 infographic (ES), existing KB files.  
> Last updated: 2026-06-19

---

## Problem statement

Current docs span ClickUp, SharePoint, Drive, GitBook, Figma, NocoDB, and Slack.  
Two journeys are almost entirely undocumented externally:  
- **Government data analysis** (Role 2: define use case, onboard dashboard users, set KPIs)  
- **ISP/partner** pathway  

The school installation journey exists but is scattered and informal-looking.

---

## Audiences (from PRD)

| Audience | Primary need | Current coverage |
|---|---|---|
| **Schools / end users** | Install, register, understand what the app does | Partial — install guide + FAQ exist |
| **UNICEF country office** | Onboard, interpret data, troubleshoot, escalation paths | Minimal |
| **Government rollout managers (Role 1)** | Device readiness, installation strategy, training, rollout monitoring, escalation | Partial — checklist + blueprint only |
| **Government data analysis leads (Role 2)** | Use case definition, dashboard access, metric literacy, KPIs, review cadence | None |
| **Ministries / policy stakeholders** | What Giga Meter measures, privacy posture, data sharing, public trust | Partial — data governance page |
| **ISPs / partner orgs** | Data flow, integration touchpoints, escalation | None |

---

## Full IA — Target State

Audience-first top-level paths. Audience routing on homepage.

```
/                          ← Homepage with role picker
/for-schools/              ← School & end-user path
/for-governments/          ← Government rollout + data path
/technical-reference/      ← Measurement, data governance, API
/support/                  ← Troubleshooting, FAQ, error codes
/release-notes/            ← Changelog
```

---

## Page inventory

### EXISTING (10 pages — keep, revise as noted)

| File | Title | Status | Notes |
|---|---|---|---|
| `README.md` | Welcome / Landing | Keep | Add role-picker cards |
| `docs/getting-started/overview.md` | About Giga & Giga Meter | Keep | Good baseline |
| `docs/installation/system-requirements.md` | System Requirements | Keep | — |
| `docs/installation/installation-guide.md` | Installation Guide | Keep | School-focused; fine |
| `docs/technical-reference/measurement-protocols.md` | Measurement Protocols | Keep | Add color threshold table |
| `docs/technical-reference/data-governance.md` | Data Governance & Privacy | Keep | — |
| `docs/troubleshooting/troubleshooting.md` | Troubleshooting | Expand | Add 5 more issues (school ID not found, app not registering after reinstall, Unknown on Giga Maps) |
| `docs/troubleshooting/faq.md` | FAQ | Expand | Merge with `GigaMeterFAQs.md`; add 6 missing entries |
| `docs/deployment/deployment-checklist.md` | Deployment Checklist | Keep | Good |
| `docs/deployment/deployment-blueprint.md` | Deployment Blueprint | Keep | Good |

---

### PHASE 1 — School journey completion (4 net-new pages)

Priority: highest. Unblocks self-service for the most common support requests.

| File | Title | Source content |
|---|---|---|
| `docs/getting-started/what-giga-meter-measures.md` | What Giga Meter Measures (and Doesn't) | v2.0.2 infographic disclaimer + measurement-protocols.md |
| `docs/getting-started/uptime-explained.md` | Uptime: What It Is and Why It Matters | v2.0.2 changelog; school hours definition |
| `docs/getting-started/giga-maps-status.md` | Reading Your School's Status on Giga Maps | `GigaMeterFAQs.md` (color description); needs color threshold values |
| `docs/support/error-messages.md` | Error Messages Reference | Distill from troubleshooting + FAQ; add "Unknown school" scenario |

---

### PHASE 2 — Government: Rollout management (Role 1) (4 net-new pages)

Content source: ClickUp doc `rk10z-63037`, Installation Strategy Template, Deployment Blueprint.

| File | Title | Source content |
|---|---|---|
| `docs/deployment/government-onboarding-overview.md` | Government Onboarding — Overview | ClickUp doc intro + two-role framing |
| `docs/deployment/device-readiness.md` | Device Readiness Checklist | Step 2 from ClickUp doc; Windows/tablet/disk space requirements |
| `docs/deployment/installation-strategies.md` | Choosing an Installation Strategy | Strategy Template (4 models + decision matrix) |
| `docs/deployment/rollout-monitoring.md` | Monitoring Your Rollout | Step 7 from ClickUp doc; rollout health metrics; escalation to Giga |

---

### PHASE 3 — Government: Data analysis (Role 2) (5 net-new pages)

Content source: ClickUp doc `rk10z-63037` (Role 2 section). Most of this is currently undocumented externally.

| File | Title | Source content |
|---|---|---|
| `docs/data/use-case-definition.md` | Defining Your Use Case | Role 2 Step 1; SVG example (ISP fines); Brazil example (1 Mbps/student) |
| `docs/data/access-channels.md` | Access Channels: Dashboard and API | Role 2 Step 3; Superset vs API distinction |
| `docs/data/dashboard-guide.md` | Using the Dashboard | Role 2 Step 3; Superset walkthrough (gap: needs screenshots or Loom) |
| `docs/data/metric-glossary.md` | Metric Glossary | Role 2 Step 4 + 5; define ~15 terms (download speed, upload speed, latency, uptime, median, benchmark, ISP, NDT-7, ping, packet loss, RTM status, Unknown, inactive, whitelisted) |
| `docs/data/kpi-guide.md` | Defining and Tracking KPIs | Role 2 Step 5 + 6; 3–5 KPI template with formula/threshold/owner/cadence |

---

### PHASE 4 — Reference and housekeeping (3 net-new pages)

| File | Title | Notes |
|---|---|---|
| `docs/release-notes/v2-0-2.md` | What's New in v2.0.2 | Uptime metric, measurement schedule changes from infographic |
| `docs/for-partners/partner-overview.md` | For ISPs and Partner Organisations | Data flow, escalation paths, no personal data sharing |
| `docs/support/escalation-paths.md` | Escalation Paths | School → CO → Giga; what to include in a support request |

---

## Prioritized writing order

```
Phase 1 (school completion)   → 4 pages   → immediately actionable, broadest audience
Phase 2 (gov rollout Role 1)  → 4 pages   → unblocks country office onboarding
Phase 3 (gov data Role 2)     → 5 pages   → highest strategic value; most underdocumented
Phase 4 (reference)           → 3 pages   → fill gaps; can be written anytime
```

**Total:** 10 existing + 16 net-new = **26 pages**

---

## Navigation update needed (docs.json)

The current `docs.json` groups are school-only. Target structure:

```json
{
  "navigation": {
    "groups": [
      {
        "group": "Get Started",
        "pages": [
          "README",
          "docs/getting-started/overview",
          "docs/getting-started/what-giga-meter-measures",
          "docs/getting-started/uptime-explained",
          "docs/getting-started/giga-maps-status"
        ]
      },
      {
        "group": "Installation",
        "pages": [
          "docs/installation/system-requirements",
          "docs/installation/installation-guide"
        ]
      },
      {
        "group": "Country Deployment",
        "pages": [
          "docs/deployment/government-onboarding-overview",
          "docs/deployment/device-readiness",
          "docs/deployment/installation-strategies",
          "docs/deployment/deployment-checklist",
          "docs/deployment/deployment-blueprint",
          "docs/deployment/rollout-monitoring"
        ]
      },
      {
        "group": "Data & Dashboard",
        "pages": [
          "docs/data/use-case-definition",
          "docs/data/access-channels",
          "docs/data/dashboard-guide",
          "docs/data/metric-glossary",
          "docs/data/kpi-guide"
        ]
      },
      {
        "group": "Technical Reference",
        "pages": [
          "docs/technical-reference/measurement-protocols",
          "docs/technical-reference/data-governance"
        ]
      },
      {
        "group": "Support",
        "pages": [
          "docs/troubleshooting/troubleshooting",
          "docs/support/error-messages",
          "docs/support/escalation-paths",
          "docs/troubleshooting/faq"
        ]
      },
      {
        "group": "Partners",
        "pages": [
          "docs/for-partners/partner-overview"
        ]
      },
      {
        "group": "Release Notes",
        "pages": [
          "docs/release-notes/v2-0-2"
        ]
      }
    ]
  }
}
```

---

## Open questions / content gaps

| Gap | Needed for | Blocked on |
|---|---|---|
| Giga Maps color thresholds (exact Mbps/latency values for red/yellow/green) | `giga-maps-status.md` + `measurement-protocols.md` | Need to confirm from product/engineering |
| Dashboard screenshots or Loom walkthrough | `dashboard-guide.md` | Need access to a live Superset instance |
| Partner/ISP escalation contact or email | `partner-overview.md` | Internal process not documented publicly |
| Multilingual variants (ES, FR, PT, MN) | All Phase 1 pages | Translation workflow TBD post-platform selection |
| v2.0.2 exact changelog (formal) | `release-notes/v2-0-2.md` | Infographic has most; confirm with product |

---

## Platform decision

Two options still in play:

| Platform | Status | Blocker |
|---|---|---|
| **GitBook** | GitHub sync connected; "No items" OAuth bug in space creation | GitBook account dropdown bug — try: disconnect/reconnect OAuth, incognito, or contact GitBook support |
| **Mintlify** | `docs.json` configured; not rendering | Unknown — local `npx mintlify dev` would isolate the issue |

Recommendation: test both with the same repo. Mintlify's `docs.json` and GitBook's `SUMMARY.md` + `.gitbook.yaml` already exist in the repo. Platform decision doesn't block content writing.
