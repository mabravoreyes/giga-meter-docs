# Government Onboarding Guide

Use this guide to plan and execute a Giga Meter deployment — from initial setup through to sustained data use. Each step links to the detailed resources for that stage.

---

## Before you start

Two prerequisites must be in place before any installation can begin:

* [ ] **School data validated on** [**Giga Maps**](https://maps.giga.global/map) — the country's schools are mapped with official government IDs and the data has been reviewed and approved by the government.
* [ ] **Country whitelisted on Giga's backend** — Giga enables the country in the system before Giga Meter can register schools. Email [gigatech@unicef.org](mailto:gigatech@unicef.org) to request whitelisting.

Contact your Giga focal point or UNICEF country office to confirm both are ready. Once confirmed, complete the [Deployment Blueprint](deployment-blueprint.md) to align your team on strategy, scope, and timeline before the rollout begins.

---

## Two roles, running in parallel from day one

A Giga Meter deployment involves two distinct workstreams. They can sit with the same department or person, but the activities are distinct and should run concurrently.

| Role | Responsible for | Typically held by |
|---|---|---|
| **Installation Lead** | Getting Giga Meter running across schools and keeping it there | MoE IT department, regional coordinators, school principals |
| **Data Analysis Lead** | Ensuring the data is used — defining use cases, onboarding users, setting KPIs | MoE planning or statistics unit |

**Both workstreams start on day one.** By the time the first schools report data, the data analysis side should already be ready to read it.

---

## Role 1 — Installation Lead

### Step 1 — Designate the installation lead

Assign clear ownership for installation at national and subnational levels. The installation lead can be the Giga Meter Project Owner or someone designated by them.

**Output:** Name, contact, and title of the installation lead (and any regional or subnational leads).

---

### Step 2 — Confirm device readiness

Before the rollout, verify that target schools meet the minimum device and connectivity conditions required for consistent data collection. Giga Meter currently runs on **Windows only** — tablets and Android devices cannot run the app.

**Output:** School-level (or sampled) check of Windows version, free disk space, and whether devices are powered on and connected during school hours.

{% hint style="warning" %}
If a school has no Windows device, flag it to Giga before the rollout. Android support is in development.
{% endhint %}

→ [Device Readiness Checklist](device-readiness.md)

---

### Step 3 — Ensure school ID matching

Installers must register the correct school ID when setting up Giga Meter. Provide guidance on what to do if a school cannot be found, if duplicates appear, or if there is a suspected mismatch — and establish a process for reporting errors to the Giga team.

**Output:** Support mechanism in place for school ID issues; escalation path to Giga documented.

---

### Step 4 — Choose an installation strategy

Choose how installations will happen based on country capacity, geography, school digital readiness, and scale. Four strategies have been used across Giga deployments — they can be combined.

| Strategy | When to use | Example |
|---|---|---|
| Expert in-person | Small scale, low school IT capacity | Honduras |
| Hybrid — regional workshops | Medium scale, regional structure | Sri Lanka |
| Guided remote | Large scale, decent school IT capacity | Belize, Albania |
| Self-installation | Very large scale, mature school IT | Brazil |

**Output:** Documented installation strategy (or combination) with rationale.

→ [Installation Strategies](installation-strategies.md)

---

### Step 5 — Establish a troubleshooting and escalation mechanism

Set up a government support layer between the installer and the Giga team. At minimum, this needs:

* A named support owner
* A basic troubleshooting runbook (common issues + first-response steps)
* A documented escalation path to Giga: who contacts whom, with what information

**Output:** Support owner named; runbook in place; Giga escalation protocol documented.

→ [Rollout Monitoring — Escalation path](rollout-monitoring.md)

---

### Step 6 — Train installers

Run one or more training sessions (virtual or in-person) and keep a support channel open throughout the rollout (e.g. WhatsApp group, email list).

**Materials available from Giga:**

* Giga Meter Onboarding deck (EN / ES)
* Workshop Checklist (EN)
* Installation Guide (EN / ES / FR / PT / MN)
* Installation videos (subtitles in EN / PT / MN)

**Output:** Installers trained; support channel open; materials available in local language.

→ [Workshop & School Checklist](deployment-checklist.md)

---

### Step 7 — Monitor the rollout

Track progress against your planned timeline and target from the day installation begins. Share monthly updates with the Giga team for the first three months, then quarterly.

**Three metrics to track from the start:**

| Metric | What it tells you |
|---|---|
| % of target schools with Giga Meter installed | Are you on pace? |
| % of installed schools reporting data in the last 7 days | Are installed schools actually collecting data? |
| Open troubleshooting tickets per week | Is the support mechanism keeping up? |

**Output:** Active rollout tracker; monthly progress update shared with Giga for the first 3 months, then quarterly.

→ [Rollout Monitoring](rollout-monitoring.md)

---

### Step 8 — Follow up with school-level focal points

Identify a responsible individual at each school to maintain the app. If a device is replaced or reformatted, Giga Meter must be reinstalled — school focal points are responsible for flagging this.

**Output:** Per-school contact list (name, role, phone/email) for maintenance and quick troubleshooting.

---

## Role 2 — Data Analysis Lead

### Step 1 — Define the use case

Before onboarding any user to the dashboard, define what the government will use Giga Meter data for. This shapes which KPIs to track and which decisions the data will inform.

**Output:** A 1-pager or short document specifying which decisions Giga Meter data will inform — e.g. "If schools are unconnected for 3 consecutive working days, the ISP is fined" (Moldova).

→ [Defining Your Use Case](../data/use-case-definition.md)

---

### Step 2 — Identify data users and assign access roles

Identify who in the ministry — and beyond — needs Giga Meter data and at what level. School-level focal points and regional coordinators may also require access.

**Output:** Named list of data users with their role, the access channel they need (dashboard or API), and the unit they sit in.

→ [Access Channels: Dashboard and API](../data/access-channels.md)

---

### Step 3 — Onboard data users to their access channels

Each identified user should be able to locate their data — school, regional, or national view — and export it independently. For dashboard users, organise a guided walkthrough (live or recorded) covering filters, comparisons, and data export.

**Output:** Every user has logged in and can independently pull the data they need for their role.

→ [Using the Dashboard](../data/dashboard-guide.md)

---

### Step 4 — Establish metric literacy

Giga Meter reports several technical metrics. Circulate a simple reference explaining what each metric means and what a good or problematic result looks like in the country's context.

**Output:** Metric glossary circulated to all data users.

→ [Metric Glossary](../data/metric-glossary.md)

---

### Step 5 — Define KPIs

Translate the use case into 3–5 measurable KPIs, each with a formula, threshold, owner, and review frequency. Share the completed KPI document with the Giga data team so they can advise on whether the standard dashboard covers your needs or requires customisation.

**Output:** KPI document shared with the Giga data team.

→ [Defining and Tracking KPIs](../data/kpi-guide.md)

---

### Step 6 — Set a KPI review and decision-triggering process

Define how often KPIs are reviewed, who runs the review, and what triggers action. Establish this process before the data starts flowing.

**Output:** Documented review process with a named meeting owner, review cadence (weekly / monthly / quarterly), and actions triggered by each KPI.

---

### Step 7 — Build capacity for ongoing analysis

Over time, government teams should be able to produce their own analyses: connectivity briefs, ISP performance reviews, and school-level investigations. If deeper analytical support is needed, contact the Giga data team.

**Output:** After 6–12 months, government users can produce and interpret analyses independently.

---

## All deployment resources

| Resource | What it's for |
|---|---|
| [Deployment Blueprint](deployment-blueprint.md) | Planning questionnaire — complete before the rollout starts |
| [Device Readiness Checklist](device-readiness.md) | School-level device and connectivity check (Step 2) |
| [Installation Strategies](installation-strategies.md) | Four approaches and how to choose (Step 4) |
| [Workshop & School Checklist](deployment-checklist.md) | Trainer guidance and school preparation materials (Step 6) |
| [Rollout Monitoring](rollout-monitoring.md) | Health metrics, reporting cadence, escalation path (Step 7) |
| [Defining Your Use Case](../data/use-case-definition.md) | How to frame what you're using the data for |
| [Access Channels: Dashboard and API](../data/access-channels.md) | Getting dashboard access and provisioning users |
| [Using the Dashboard](../data/dashboard-guide.md) | Screen-by-screen dashboard walkthrough |
| [Metric Glossary](../data/metric-glossary.md) | Definitions for every metric |
| [Defining and Tracking KPIs](../data/kpi-guide.md) | KPI framework and templates |
