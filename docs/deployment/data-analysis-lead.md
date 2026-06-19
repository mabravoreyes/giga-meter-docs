# Data Analysis Lead — Step-by-step Guide

This guide is for the government official responsible for ensuring Giga Meter data is used — from defining what to measure through to embedding analysis in ongoing decision-making. Work through these steps in parallel with the installation workstream.

← [Government Onboarding Guide](government-onboarding-overview.md)

---

## Step 1 — Define the use case

Before onboarding any user to the dashboard, define what the government will use Giga Meter data for. This shapes which KPIs to track and which decisions the data will inform.

A use case is not a general goal ("understand school connectivity") — it is a specific decision loop: what condition triggers a review, who reviews it, and what action results. Examples: flagging schools whose download speed drops below 5 Mbps for two consecutive weeks for ISP follow-up; identifying schools with no data for 30+ days for reinstallation outreach.

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

## Step 2 — Identify data users and assign access roles

Identify who in the ministry — and beyond — needs Giga Meter data and at what level. Not everyone needs the same access. School-level focal points may need to see their own school on Giga Maps; regional coordinators may need a filtered view of their region; ministry analysts may need national export access.

**Output:** Share this list with the Giga team when requesting access provisioning.

| Name | Role | Unit | Access channel | Notes |
|---|---|---|---|---|
| | | | Dashboard / API / Giga Maps | e.g. national view only |

→ [Access Channels: Dashboard and API](../data/access-channels.md)

---

## Step 3 — Onboard data users to their access channels

Each identified user should be able to locate their data — school, regional, or national view — and export it independently. For dashboard users, organise a guided walkthrough (live or recorded) covering filters, comparisons, and data export. For Giga Maps users, show them how to find their school and read the connectivity dot.

Run onboarding before the first formal data review — do not let the first time users see the data be in a meeting where they are expected to interpret it.

**Output:** Every identified user has logged in and can independently pull the data they need for their role.

{% hint style="info" %}
**Onboarding milestone**\
Onboarding session format: \[e.g. live walkthrough, recorded video, written guide]\
Date completed:\
Users onboarded: \[N]\
Users pending: \[N — names and reason for delay]
{% endhint %}

→ [Using the Dashboard](../data/dashboard-guide.md)

---

## Step 4 — Establish metric literacy

Giga Meter reports several technical metrics — download speed, upload speed, latency, and uptime. Before users start drawing conclusions from the data, circulate a simple reference explaining what each metric means and what a good or problematic value looks like in the country's context.

Context matters. A 5 Mbps download speed may be poor for a school with 200 students but adequate for a rural primary with 30. Setting country-specific or school-type-specific thresholds makes the data more actionable than global benchmarks alone.

**Output:** Metric reference document circulated to all data users before the first review meeting.

{% hint style="info" %}
**Metric reference — \[Country]**\
Download speed: what it measures / country context / threshold for concern\
Upload speed: what it measures / country context / threshold for concern\
Latency: what it measures / country context / threshold for concern\
Uptime: what it measures / country context / threshold for concern
{% endhint %}

→ [Metric Glossary](../data/metric-glossary.md)

---

## Step 5 — Define KPIs

Translate the use case into 3–5 measurable KPIs, each with a formula, threshold, owner, and review frequency. Keep the KPI set small enough to be actionable — a list of 15 indicators will not be reviewed consistently.

Share the completed KPI document with the Giga data team so they can advise on whether the standard dashboard covers your needs or requires customisation.

**Output:** Completed KPI document shared with the Giga data team.

| KPI name | Formula | Threshold | Owner | Review cadence | Action triggered |
|---|---|---|---|---|---|
| | | | | | |

→ [Defining and Tracking KPIs](../data/kpi-guide.md)

---

## Step 6 — Set a KPI review and decision-triggering process

Define how often KPIs are reviewed, who runs the review, and what triggers action. Establish this process before the data starts flowing — not after. The most common failure mode is waiting until data exists before deciding what to do with it.

The review format does not need to be elaborate. A standing 30-minute monthly call with a shared dashboard view is more sustainable than a quarterly report that takes two weeks to produce.

**Output:** Document and circulate the review process to all data users before the first data is available.

{% hint style="info" %}
**KPI review process**\
Meeting owner:\
Review cadence: \[weekly / monthly / quarterly]\
Format: \[e.g. standing call, shared dashboard, written brief]\
\
**KPI thresholds and triggers**\
\[KPI name] — threshold: \[value] — action: \[what happens]\
\[KPI name] — threshold: \[value] — action: \[what happens]\
\[KPI name] — threshold: \[value] — action: \[what happens]
{% endhint %}

---

## Step 7 — Build capacity for ongoing analysis

Over time, government teams should be able to produce their own analyses without Giga support: school-level connectivity briefs, ISP performance comparisons, regional coverage reports, and trend analysis over time.

Start small. In the first year, the goal is for the team to be able to answer basic questions from the dashboard independently — which schools are performing well, which have dropped off, and whether the situation has improved since the last review period. Deeper analytical capability — regression analysis, custom indicators, API-based reporting — can follow as familiarity grows.

If deeper support is needed at any stage, contact the Giga data team.

**Output:** After 6–12 months, government users can produce and interpret analyses independently without prompting from Giga.

{% hint style="info" %}
**Capacity milestone — \[Date]**\
Team can independently access and filter dashboard: Yes / No\
Team has produced at least one connectivity brief: Yes / No\
Team has reviewed ISP performance data: Yes / No\
Analytical support still needed from Giga: \[describe if applicable]
{% endhint %}

---

## Related pages

* [Government Onboarding Guide](government-onboarding-overview.md)
* [Defining Your Use Case](../data/use-case-definition.md)
* [Access Channels: Dashboard and API](../data/access-channels.md)
* [Using the Dashboard](../data/dashboard-guide.md)
* [Metric Glossary](../data/metric-glossary.md)
* [Defining and Tracking KPIs](../data/kpi-guide.md)
