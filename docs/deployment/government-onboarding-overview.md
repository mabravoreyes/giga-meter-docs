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

The installation lead is the named person accountable for the Giga Meter rollout in the country. They coordinate the installer network, manage troubleshooting escalations, and are the primary point of contact between the government and Giga during the rollout.

Where the rollout spans multiple regions, each region should also have a named subnational lead.

**Output:** Share the following with your Giga focal point before the rollout begins:

{% hint style="info" %}
**National Installation Lead**\
Name:\
Title:\
Unit:\
Email / phone:

**Subnational leads** *(if applicable)*\
\[Region] — Name, Title, contact\
\[Region] — Name, Title, contact
{% endhint %}

---

### Step 2 — Confirm device readiness

Before the rollout, verify that target schools meet the minimum device and connectivity conditions required for consistent data collection. Giga Meter currently runs on **Windows only** — tablets and Android devices cannot run the app.

**Output:** Complete one row per school and share with your Giga focal point before the rollout begins.

{% hint style="info" %}
| School name | School ID | Windows version | Free disk space ≥ 500 MB | Powered on during school hours | Admin rights available | Notes |
|---|---|---|---|---|---|---|
| | | | Yes / No | Yes / No | Yes / No | |
{% endhint %}

{% hint style="warning" %}
If a school has no Windows device, flag it to Giga before the rollout. Android support is in development.
{% endhint %}

→ [Device Readiness Checklist](device-readiness.md)

---

### Step 3 — Ensure school ID matching

Installers must register the correct school ID when setting up Giga Meter. Provide guidance on what to do if a school cannot be found, if duplicates appear, or if there is a suspected mismatch — and establish a process for reporting errors to the Giga team.

**Output:** Document the following and share with installers before the rollout:

{% hint style="info" %}
**School ID support**\
Installer support contact: [Name, phone / email]\
If school is not found: [instructions — e.g. check spelling, try partial ID, contact support]\
If duplicates appear: [instructions — e.g. select the one matching official school records, flag to support]\
To report a mismatch to Giga: [email / process]
{% endhint %}

---

### Step 4 — Choose an installation strategy

Choose how installations will happen based on country capacity, geography, school digital readiness, and scale. Four strategies have been used across Giga deployments — they can be combined.

| Strategy | When to use | Example |
|---|---|---|
| Expert in-person | Small scale, low school IT capacity | Honduras |
| Hybrid — regional workshops | Medium scale, regional structure | Sri Lanka |
| Guided remote | Large scale, decent school IT capacity | Belize, Albania |
| Self-installation | Very large scale, mature school IT | Brazil |

**Output:** Document the following and share with the Giga team:

{% hint style="info" %}
**Installation strategy**\
Chosen strategy: [Expert in-person / Hybrid / Guided remote / Self-installation / combination]\
Rationale: [brief explanation based on scale, geography, school IT capacity]\
Target schools: [N]\
Coverage breakdown: [e.g. by region or school type if using a mix]\
Installer support channel: [e.g. WhatsApp group, email list, help desk]
{% endhint %}

→ [Installation Strategies](installation-strategies.md)

---

### Step 5 — Establish a troubleshooting and escalation mechanism

Set up a government support layer between the installer and the Giga team. At minimum, this needs:

* A named support owner
* A basic troubleshooting runbook (common issues + first-response steps)
* A documented escalation path to Giga: who contacts whom, with what information

**Output:** Document the escalation protocol and circulate to all installers:

{% hint style="info" %}
**Troubleshooting & escalation protocol**\
Government support owner: [Name, phone / email]\
When to escalate to government support: [e.g. issue not resolved by installer within 24h]\
Giga escalation contact: [Name / email at UNICEF country office]\
When to escalate to Giga: [e.g. issue unresolved at government level after 48h]\
Information to include when escalating: school name and ID, Giga Meter version, error message or screenshot, steps already attempted
{% endhint %}

→ [Rollout Monitoring — Escalation path](rollout-monitoring.md)

---

### Step 6 — Train installers

Run one or more training sessions (virtual or in-person) and keep a support channel open throughout the rollout (e.g. WhatsApp group, email list).

**Materials available from Giga:**

* Giga Meter Onboarding deck (EN / ES)
* Workshop Checklist (EN)
* Installation Guide (EN / ES / FR / PT / MN)
* Installation videos (subtitles in EN / PT / MN)

**Output:** Confirm the following before the first installation session:

{% hint style="info" %}
**Training plan**\
Training format: [e.g. Zoom webinar / in-person workshop / regional sessions]\
Date(s):\
Materials language(s):\
Installer support channel: [e.g. WhatsApp group name / help desk email]
{% endhint %}

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

**Output:** Share a monthly update with the Giga team using this format:

{% hint style="info" %}
**Monthly rollout update — [Month, Year]**\
Target schools: [N]\
Schools installed: [N] ([%])\
Schools reporting in the last 7 days: [N] ([%])\
Open troubleshooting tickets: [N]\
Main blockers:\
Next steps:
{% endhint %}

→ [Rollout Monitoring](rollout-monitoring.md)

---

### Step 8 — Follow up with school-level focal points

Identify a responsible individual at each school to maintain the app. If a device is replaced or reformatted, Giga Meter must be reinstalled — school focal points are responsible for flagging this.

**Output:** Maintain a registry of school focal points, updated whenever contacts change:

{% hint style="info" %}
| School name | School ID | Focal point name | Role | Phone / email |
|---|---|---|---|---|
| | | | | |
{% endhint %}

---

## Role 2 — Data Analysis Lead

### Step 1 — Define the use case

Before onboarding any user to the dashboard, define what the government will use Giga Meter data for. This shapes which KPIs to track and which decisions the data will inform.

**Output:** A short document specifying which decisions Giga Meter data will inform. Share with the Giga team before the first dashboard onboarding session.

{% hint style="info" %}
**Use case definition**\
What we are monitoring:\
Threshold or condition that signals a problem:\
Who is responsible for acting on it:\
What action is taken:\
How often is it reviewed:
{% endhint %}

→ [Defining Your Use Case](../data/use-case-definition.md)

---

### Step 2 — Identify data users and assign access roles

Identify who in the ministry — and beyond — needs Giga Meter data and at what level. School-level focal points and regional coordinators may also require access.

**Output:** Share this list with the Giga team when requesting access provisioning:

{% hint style="info" %}
| Name | Role | Unit | Access channel | Notes |
|---|---|---|---|---|
| | | | Dashboard / API | e.g. national view only |
{% endhint %}

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

**Output:** Share the completed KPI document with the Giga data team:

{% hint style="info" %}
| KPI name | Formula | Threshold | Owner | Review cadence | Action triggered |
|---|---|---|---|---|---|
| | | | | | |
{% endhint %}

→ [Defining and Tracking KPIs](../data/kpi-guide.md)

---

### Step 6 — Set a KPI review and decision-triggering process

Define how often KPIs are reviewed, who runs the review, and what triggers action. Establish this process before the data starts flowing.

**Output:** Document and circulate the review process to all data users:

{% hint style="info" %}
**KPI review process**\
Meeting owner:\
Review cadence: [weekly / monthly / quarterly]\
Format: [e.g. standing meeting, shared dashboard, written brief]\
KPI | Threshold | Action triggered\
[KPI name] | [threshold] | [action]
{% endhint %}

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
