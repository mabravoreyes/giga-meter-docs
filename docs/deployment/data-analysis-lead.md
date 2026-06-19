# Data Analysis Lead — Step-by-step Guide

This guide is for the government official responsible for ensuring Giga Meter data is used — from defining what to measure through to embedding analysis in ongoing decision-making. Work through these steps in parallel with the installation workstream.

← [Government Onboarding Guide](government-onboarding-overview.md)

---

## Step 1 — Define the use case

Before onboarding any user to the dashboard, define what the government will use Giga Meter data for. This shapes which KPIs to track and which decisions the data will inform.

A use case is not a general goal ("understand school connectivity") — it is a specific decision loop: what condition triggers a review, who reviews it, and what action results.

{% hint style="warning" %}
Without a defined use case, dashboard users tend to look at the data without knowing what to do with it. The use case definition is the foundation of the entire data analysis workstream.
{% endhint %}

**A use case answers three questions:**

1. **What decision will this data inform?** e.g. which schools to prioritise for ISP upgrades; whether a provider is meeting contract terms; whether a national connectivity target is on track
2. **Who makes that decision?** e.g. the MoE IT unit, the planning department, the minister
3. **How often is that decision made?** e.g. monthly for operational reviews, annually for budget planning

**Examples from Giga deployments:**

| Country | Use case | Decision triggered |
|---|---|---|
| Brazil | National Connected Schools Strategy — target: 1 Mbps per student in the longest shift | Schools below threshold flagged for ISP renegotiation |
| Moldova | ISP contract enforcement | If a school is unconnected for 3 consecutive working days, the ISP is fined |
| General | Deployment monitoring | Schools not reporting within 7 days get a follow-up call from the regional coordinator |

**Writing your use case**

Aim for one paragraph. It should answer: what is being monitored, what counts as a problem, and who acts on it.

> *"We are using Giga Meter to monitor whether schools in the northern region are receiving the minimum contracted speed of 10 Mbps. Schools below this threshold for two consecutive weeks are reported to the regional ISP coordinator for follow-up. Reports are reviewed monthly by the MoE IT department."*

**Connecting use case to KPIs**

Once the use case is clear, define the KPIs that operationalise it — see Step 5.

| Use case type | Typical KPIs |
|---|---|
| Policy enforcement | % schools meeting national speed benchmark; # schools below benchmark for 30+ consecutive days |
| ISP service monitoring | % schools where measured speed is within X% of contracted speed |
| Deployment tracking | % schools with active Giga Meter data; % reporting in the last 7 days |
| Baseline and trend analysis | Average download speed per district per quarter; YoY change in median latency |

**Output:** A short document specifying which decisions Giga Meter data will inform. Share with the Giga team before the first dashboard onboarding session.

{% hint style="info" %}
**Use case definition**\
What we are monitoring:\
Threshold or condition that signals a problem:\
Who is responsible for acting on it:\
What action is taken:\
How often is it reviewed:
{% endhint %}

---

## Step 2 — Identify data users and assign access roles

Identify who in the ministry — and beyond — needs Giga Meter data and at what level. Not everyone needs the same access. School-level focal points may need to see their own school on Giga Maps; regional coordinators may need a filtered view of their region; ministry analysts may need national export access.

**Common access patterns:**

| Role | Typical channel | Access scope |
|---|---|---|
| Planning director / minister | Dashboard | National view |
| MoE IT coordinator | Dashboard + API | All schools |
| Regional coordinator | Dashboard | Regional filter only |
| School focal point | Giga Maps | Own school only |
| Technical partner / data analyst | API | Full export |

**Output:** Share this list with the Giga team when requesting access provisioning.

| Name | Role | Unit | Access channel | Notes |
|---|---|---|---|---|
| | | | Dashboard / API / Giga Maps | e.g. national view only |

---

## Step 3 — Onboard data users to their access channels

Giga Meter data is accessible through two channels. Which channel a user needs depends on how they work with data.

| Channel | Best for | Access |
|---|---|---|
| **Superset Dashboard** | Policy teams, ministry staff, country coordinators — people who need charts and tables without writing code | Login credentials provisioned by Giga |
| **API** | Technical teams, data analysts, partners who want to integrate Giga data into their own systems or run custom analyses | API key provisioned by Giga |
| **Giga Maps** | Schools, regional focal points, and the public — viewing a school's connectivity dot | Public — no credentials needed |

Both channels access the same underlying data. The difference is presentation and flexibility.

**Superset Dashboard**

The dashboard provides seven pre-built screens covering school-level summaries, speed and latency trends, district breakdowns, per-measurement data tables, app version tracking, and installation health.

*Getting access:* Contact your Giga focal point or the UNICEF country office. Provide the name, role, and email of each user who needs access.

*What users can do:* filter by school, district, date range, and education level; export any table to CSV; view time series, box plots, and distribution charts; share direct links to specific dashboard views.

*What users cannot do:* edit the dashboard or charts (read-only); access data from other countries.

**API**

The Giga Maps API provides programmatic access to school connectivity data — for teams that want to pull data into their own tools, build automated reports, or integrate Giga data into government systems.

*Getting access:* Contact the Giga team through your UNICEF country focal point to request an API key and documentation.

*What the API provides:* school-level measurements (download speed, upload speed, latency, uptime); school metadata (location, education level, government ID); time-series data queryable by school, district, and date range; data licensed under CC BY 4.0.

**Run onboarding before the first data review.** Do not let the first time users see the data be in a meeting where they are expected to interpret it.

**Output:** Every identified user has logged in and can independently pull the data they need for their role.

{% hint style="info" %}
**Onboarding milestone**\
Onboarding session format: \[e.g. live walkthrough, recorded video, written guide]\
Date completed:\
Users onboarded: \[N]\
Users pending: \[N — names and reason for delay]
{% endhint %}

**Dashboard screens — reference**

The dashboard has seven screens, accessible from the tab bar at the top.

| Screen | What it answers |
|---|---|
| **Summary** | How many schools are on the map, how many report through Giga Meter, and headline speed and latency figures |
| **Connectivity · Speed & Latency** | Daily speed and latency trends, and how speeds are distributed across schools |
| **Connectivity · District** | Average speed broken out by district, plus a per-school table with sparklines |
| **Data Tables · Registered** | One row per registered school — key operational fields for follow-up |
| **Data Tables · Measurements** | One row per individual test, including Wi-Fi diagnostics captured at measurement time |
| **App Tracking** | Which Giga Meter version is running across the country; daily reporting counts |
| **Installation Tracking** | Who's live, who's gone quiet, and drop-off rate by district |

<details>

<summary>Screen 1 — Summary</summary>

The opening view. Two big numbers — schools on the map and schools reporting through Giga Meter — followed by headline speed and latency figures.

| What you see | Term | What it means |
|---|---|---|
| Schools on Giga Maps (e.g. 1.19k) | Giga Maps | Schools that have been located and published on Giga Maps |
| Schools with Giga Meter (e.g. 81) | Giga Meter | Of the mapped schools, how many run the app and stream measurements |
| Live (e.g. 75) | Live school | Schools that sent a reading within the last 21 days |
| Drop-off (e.g. 5) | Drop-off | Schools silent for 28+ days — unlikely to come back without a site visit |
| At-risk (e.g. 1) | At-risk school | Schools in the 21–28-day quiet window |
| Average download (e.g. 85.59 Mbps) | Download speed | Average across all schools and all measurements in scope |
| Average latency (e.g. 59 ms) | Latency | About the upper edge of what feels instant in a video call |
| Total measurements (e.g. 32.4k) | Measurement | Individual Giga Meter tests across all schools in the selected time window |

</details>

<details>

<summary>Screen 2 — Connectivity · Speed & Latency</summary>

Daily speed and latency trends, plus box-plot distributions showing how consistent the experience is across schools.

| What you see | Term | What it means |
|---|---|---|
| Black line | Download speed | Average daily download, in Mbps |
| Blue line | Upload speed | Average daily upload — usually below download |
| Box plot | Speed distribution | Shaded box = middle 50% of schools; dots = outliers |
| Lower chart | Latency | Average daily latency in milliseconds |
| Y-axis unit | Milliseconds (ms) | Under 50 ms comfortable for video calls; over 200 ms causes noticeable lag |

</details>

<details>

<summary>Screen 3 — Connectivity · District</summary>

Average speed broken out by administrative district, then a per-school table with sparklines.

| What you see | Term | What it means |
|---|---|---|
| Grey bars | Download speed | Average download per district |
| Green bars | Upload speed | Side-by-side with download — makes asymmetric links easy to spot |
| "Last value" column | Load speed | The most recent single Giga Meter test reading |
| "Weekly Avg" column | Rolling average | Average of every measurement from the last seven days |
| "WoW %" column | Week-over-Week % | −91% means this week's average is 91% lower than last week — worth investigating |

</details>

<details>

<summary>Screen 4 — Data Tables · Registered</summary>

One row per school that has registered through Giga Meter. Most useful for operational follow-up.

| Column name | What it means |
|---|---|
| `school_id_govt` | The country's official school identifier — different from Giga's internal ID |
| `num_measurements` | Total Giga Meter tests the school has ever run |
| Days since last measurement | 0 = sent a reading today; non-zero is an early warning |
| `num_devices_registered` | How many computers at the school are linked to Giga Meter |
| `most_recent_app_version` | Newest Giga Meter build any device at the school is running |

{% hint style="success" %}
Sort by "days since last measurement" descending to surface schools that need follow-up first.
{% endhint %}

</details>

<details>

<summary>Screen 5 — Data Tables · Measurements</summary>

One row per individual Giga Meter test, including Wi-Fi diagnostics captured at measurement time.

| Column name | What it means |
|---|---|
| `load_speed` | Download speed recorded by this specific test, in Mbps |
| `isp_asn_clean` | Identifies which provider's network served this test |
| `avg_latency` | Latency recorded by this specific test, in ms |
| `isp_clean` | ISP name, cleaned from what the app captured |
| `detected_wifi_ssid` | Name of the Wi-Fi network the device was on during the test |
| Wi-Fi signal | Signal strength in dBm — closer to zero is stronger (−60 healthy; −85 weak) |
| Wi-Fi TX rate | Data rate to the router in Mbps — drops as wireless link weakens |

{% hint style="info" %}
If a school shows low `load_speed` but healthy latency and strong Wi-Fi signal, the bottleneck is likely on the ISP side, not the school's internal network.
{% endhint %}

</details>

<details>

<summary>Screen 6 — App Tracking</summary>

Which version of Giga Meter is deployed across the country and how many schools send data each day.

| What you see | What it means |
|---|---|
| Donut chart | Each wedge = a different Giga Meter build. A single wedge = uniform version |
| Bar chart | Each bar = number of schools that sent at least one measurement that day |
| Grey line | 7-day rolling count — smooths weekend dips and reveals growth trend |

{% hint style="success" %}
After a version update, watch this screen for schools still on older builds. A fragmented donut means some devices missed the update.
{% endhint %}

</details>

<details>

<summary>Screen 7 — Installation Tracking</summary>

Health-check view. Shows who's live, who's gone quiet, and drop-off rate by district.

| What you see | What it means |
|---|---|
| Live schools count | Schools that sent a measurement in the last 21 days |
| Drop-off count | Schools silent for 28+ days — without intervention unlikely to return |
| Drop-off rate | Drop-offs ÷ total installed schools. Rising rate = support effort needed |

{% hint style="warning" %}
A drop-off rate above 10% is a signal to increase follow-up with school IT focal points or to plan re-installation visits.
{% endhint %}

</details>

---

## Step 4 — Establish metric literacy

Giga Meter reports several technical metrics. Before users start drawing conclusions from the data, circulate a simple reference explaining what each metric means and what a good or problematic value looks like in the country's context.

Context matters. A 5 Mbps download speed may be poor for a school with 200 students but adequate for a rural primary with 30. Setting country-specific or school-type-specific thresholds makes the data more actionable than global benchmarks alone.

**Key metrics:**

| Metric | What it measures | As a rough guide |
|---|---|---|
| **Download speed** (Mbps) | Rate at which the school receives data from the internet | 1 Mbps per participant for audio calls; 5 Mbps+ for HD video per class |
| **Upload speed** (Mbps) | Rate at which the school sends data — the outgoing side of a video call | Usually lower than download; asymmetric links are normal |
| **Latency** (ms) | Delay between a request and the first response | Under 50 ms feels instant; over 200 ms causes noticeable lag |
| **Uptime** (%) | Share of school hours (8 AM–8 PM) where the connection is confirmed active | 99% = down at most ~7 hours/month |
| **Live school** | Last measurement within 21 days | Device actively reporting |
| **At-risk school** | Last measurement 21–28 days ago | May drop off without follow-up |
| **Drop-off** | No measurement in 28+ days | Unlikely to return without a site visit |
| **Drop-off rate** | Drop-offs ÷ total installed schools | Above 10% = increase follow-up effort |

For full definitions of every field in the dashboard, see [Metric Glossary](../technical-reference/metric-glossary.md).

**Output:** Metric reference document circulated to all data users before the first review meeting.

{% hint style="info" %}
**Metric reference — \[Country]**\
Download speed: what it measures / country context / threshold for concern\
Upload speed: what it measures / country context / threshold for concern\
Latency: what it measures / country context / threshold for concern\
Uptime: what it measures / country context / threshold for concern
{% endhint %}

---

## Step 5 — Define KPIs

Translate the use case into 3–5 measurable KPIs, each with a formula, threshold, owner, and review frequency. Keep the KPI set small enough to be actionable — a list of 15 indicators will not be reviewed consistently.

**Each KPI needs:**

| Field | Description |
|---|---|
| **Name** | Short, descriptive label |
| **Formula** | Exactly how the number is calculated |
| **Threshold** | What counts as "good" vs. "a problem" |
| **Owner** | Who monitors and acts on this KPI |
| **Review cadence** | How often it is reviewed |
| **Action triggered** | What happens when the threshold is breached |

**Examples:**

<details>

<summary>Policy enforcement — % schools meeting national speed benchmark</summary>

| | |
|---|---|
| **Formula** | Schools with 30-day average download speed ≥ \[national threshold] Mbps ÷ total schools with active Giga Meter × 100 |
| **Threshold** | ≥ 80% on track; < 60% escalate to ISP unit |
| **Owner** | MoE IT Department |
| **Review cadence** | Monthly |
| **Action triggered** | Schools below threshold for 30+ consecutive days reported to ISP coordinator |

</details>

<details>

<summary>ISP performance monitoring — % schools receiving contracted speed</summary>

| | |
|---|---|
| **Formula** | Schools where measured speed ≥ 80% of contracted Mbps ÷ schools with known contract × 100 |
| **Threshold** | < 70% compliance = formal notice to ISP |
| **Owner** | Procurement / legal unit |
| **Review cadence** | Monthly |
| **Action triggered** | Formal notice to ISP; repeated failure triggers contract review |

</details>

<details>

<summary>Deployment health — % installed schools actively reporting</summary>

| | |
|---|---|
| **Formula** | Schools that sent ≥ 1 measurement in the last 7 days ÷ schools with Giga Meter installed × 100 |
| **Threshold** | < 70% = increase follow-up; < 50% = escalate to Giga |
| **Owner** | Installation lead |
| **Review cadence** | Weekly for first 3 months, then monthly |
| **Action triggered** | Contact silent schools; flag persistent drop-offs to Giga |

</details>

Share the completed KPI document with the Giga data team. If your KPIs require dashboard customisation — a column not yet in the standard view — the team will advise on feasibility and timeline.

**Output:** Completed KPI document shared with the Giga data team.

| KPI name | Formula | Threshold | Owner | Review cadence | Action triggered |
|---|---|---|---|---|---|
| | | | | | |

---

## Step 6 — Set a KPI review and decision-triggering process

Define how often KPIs are reviewed, who runs the review, and what triggers action. Establish this process before the data starts flowing — not after. The most common failure mode is waiting until data exists before deciding what to do with it.

The review format does not need to be elaborate. A standing 30-minute monthly call with a shared dashboard view is more sustainable than a quarterly report that takes two weeks to produce. Countries that define this process upfront are more likely to use Giga Meter data consistently over time. Countries that leave it informal tend to use the data reactively, only when a crisis prompts them.

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
* [Deployment Blueprint](deployment-blueprint.md)
* [Installation Lead Guide](installation-lead.md)
* [Metric Glossary](../technical-reference/metric-glossary.md)
* [Measurement Protocols](../technical-reference/measurement-protocols.md)
* [Data Governance & Privacy](../technical-reference/data-governance.md)
