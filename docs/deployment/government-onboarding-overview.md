# Government Onboarding Guide

Use this guide to plan and execute a Giga Meter deployment — from initial setup through to sustained data use. Each step links to the detailed resources for that stage.

***

## Before you start

Two prerequisites must be in place before any installation can begin:

* [ ] **School data validated on** [**Giga Maps**](https://maps.giga.global/map) — the country's schools are mapped with official government IDs and the data has been reviewed and approved by the government.
* [ ] **Country whitelisted on Giga's backend** — Giga enables the country in the system before Giga Meter can register schools. Email [gigatech@unicef.org](mailto:gigatech@unicef.org) to request whitelisting.

Contact your Giga focal point or UNICEF country office to confirm both are ready. Once confirmed, complete the [Deployment Blueprint](deployment-blueprint.md) to align your team on strategy, scope, and timeline before the rollout begins.

***

## Two roles, running in parallel from day one

A Giga Meter deployment involves two distinct workstreams. They can sit with the same department or person, but the activities are distinct and should run concurrently.

| Role                   | Responsible for                                                                | Typically held by                                           |
| ---------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **Installation Lead**  | Getting Giga Meter running across schools and keeping it there                 | MoE IT department, regional coordinators, school principals |
| **Data Analysis Lead** | Ensuring the data is used — defining use cases, onboarding users, setting KPIs | MoE planning or statistics unit                             |

**Both workstreams start on day one.** By the time the first schools report data, the data analysis side should already be ready to read it.

***

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

**Subnational leads** _(if applicable)_\
\[Region] — Name, Title, contact
{% endhint %}

***

### Step 2 — Define target schools and phasing

Agree on which schools will receive Giga Meter and in what order before the rollout begins. The total number and selection criteria determine the installation strategy, the installer network size, and the monitoring workload.

**Pilot first, then scale**

Start with a small pilot cohort — typically 10–30 schools — before expanding nationally. The pilot validates the installation process, surfaces issues in the support channel, and gives the data analysis team real data to work with before the full rollout.

Select pilot schools to represent the range of your national target: mix urban and rural, include different regions, and include at least some schools with lower IT capacity. Avoid selecting only the easiest schools — pilots that go too smoothly don't surface the friction that will slow down the national rollout.

**Phasing the scale-up**

After the pilot, expand in phases rather than attempting a single national rollout. Common phasing approaches:

| Approach | How it works | Works best when |
|---|---|---|
| By region | Roll out region by region, using regional focal points | You have a clear regional structure |
| By school type | Start with secondary schools, then primary | Device readiness varies significantly by school type |
| By connectivity tier | Start with better-connected schools to build early data coverage | You want to demonstrate value quickly |
| By partner | Delegate phases to regional education offices or NGO partners | You have a distributed implementation network |

Phases can overlap — the next phase can begin before the previous one is complete, as long as the support channel can absorb the additional load.

**Output:** Share the following with the Giga team before the rollout begins:

{% hint style="info" %}
**Target schools and phasing plan**\
Total target schools: \[N]\
Selection criteria: \[e.g. schools with Windows devices, mapped on Giga Maps, specific regions or school types]\
\
**Pilot**\
Schools: \[N] — \[selection rationale]\
Timeline: \[start – end date]\
\
**Phase 2**\
Schools: \[N] — \[scope: region / school type / partner]\
Timeline: \[start – end date]\
\
**Phase 3** *(if applicable)*\
Schools: \[N] — \[scope]\
Timeline: \[start – end date]
{% endhint %}

***

### Step 3 — Confirm device readiness

Before the rollout, verify that target schools meet the minimum device and connectivity conditions required for consistent data collection.&#x20;

{% hint style="warning" %}
If a school has no Windows device, flag it to Giga before the rollout. Android support is in development.
{% endhint %}

* [ ] **Windows OS** — Windows 7 or higher (desktop or laptop)
* [ ] **Free disk space** — at least 500 MB available
* [ ] **Regular use** — device is used daily or near-daily (a device that is rarely powered on will collect very little data)
* [ ] **Dedicated school connection** — device connects exclusively to the school's internet, not a mobile hotspot or personal router
* [ ] **Admin rights available** — the person installing Giga Meter can approve the installation (admin password or IT approval in hand)

***

### Step 4 — Ensure school IDs are known by installers

Each school in Giga Meter is registered using an official school ID. Before the rollout, make sure the training covers what the school ID looks like in the country's system and where installers can look it up. Include a named support contact for cases where the school cannot be found or the ID appears incorrect.

**Output:** Include the following in installer training materials:

{% hint style="info" %}
**School ID reference**\
What the school ID looks like: \[e.g. format, example — "BR12345"]\
Where to find it: \[e.g. national school registry, MoE database, letter from the ministry]\
Support contact for ID issues: \[Name, phone / email]
{% endhint %}

***

### Step 5 — Choose an installation strategy

Choose how installations will happen based on country capacity, geography, school digital readiness, and scale. Four strategies have been used across Giga deployments — they can be combined.

{% tabs %}
{% tab title="Expert in-person" %}
<figure><img src="../../.gitbook/assets/strategy-expert-inperson.png" alt="Expert in-person installation" width="180"><figcaption></figcaption></figure>

**When to use:** Small scale, or schools with low IT capacity.

Government-trained staff visit each school, install Giga Meter themselves, and provide hands-on support to the school focal point.

**Steps:**

1. Identify staff who will visit schools for installation.
2. Develop a deployment plan with scope, timeline, and assigned schools per installer.
3. Train installation staff — in-person or virtually.
4. During installation, collect focal point contact details for maintenance and troubleshooting.
5. Set up a support channel for schools (e.g. hotline, WhatsApp group).
6. Monitor rollout and follow up with schools that fail to install.
{% endtab %}

{% tab title="Hybrid — regional workshops" %}
<figure><img src="../../.gitbook/assets/strategy-hybrid.png" alt="Hybrid regional workshop installation" width="180"><figcaption></figcaption></figure>

**When to use:** Medium scale, with a regional structure.&#x20;

School IT staff attend regional training workshops and then carry out installation at their own school.

**Steps:**

1. Adapt and share the installation guide with school principals.
2. Ask schools to nominate 1–2 focal points responsible for installation and maintenance.
3. Organise in-person regional workshops — guide focal points live through the installation.
4. Set up a support channel (hotline or help desk) for post-workshop troubleshooting.
5. Monitor rollout and follow up with schools that fail to install.
{% endtab %}

{% tab title="Guided remote" %}
<figure><img src="../../.gitbook/assets/strategy-guided-remote.png" alt="Guided remote installation" width="180"><figcaption></figcaption></figure>

**When to use:** Larger scale, schools with decent IT capacity.&#x20;

School focal points install Giga Meter themselves, supported through virtual training sessions and remote troubleshooting.

**Steps:**

1. Adapt and share the installation guide with school principals.
2. Ask schools to nominate 1–2 focal points responsible for installation and maintenance.
3. Organise virtual sessions — guide focal points live through the installation.
4. Set up a support channel (hotline or help desk) for post-session troubleshooting.
5. Monitor rollout and follow up with schools that fail to install.
{% endtab %}

{% tab title="Self-installation" %}
<figure><img src="../../.gitbook/assets/strategy-self-install.png" alt="Self-installation" width="180"><figcaption></figcaption></figure>

**When to use:** Large scale, schools with mature IT capacity.&#x20;

Schools install Giga Meter independently using the installation guide, with optional support via a help desk.

**Steps:**

1. Ensure school contact information is up to date.
2. Customise and share the installation guide with schools. Set a clear deadline.
3. Set up a support channel (hotline or help desk) for troubleshooting.
4. Monitor rollout and follow up with schools that miss the deadline.
{% endtab %}
{% endtabs %}

**Output:** Document the following and share with the Giga team:

{% hint style="info" %}
**Installation strategy**\
Chosen strategy: \[Expert in-person / Hybrid / Guided remote / Self-installation / combination]\
Rationale: \[brief explanation based on scale, geography, school IT capacity]\
Target schools: \[N]\
Coverage breakdown: \[e.g. by region or school type if using a mix]
{% endhint %}

→ [Installation Strategies](/broken/pages/m5tRNjSriTnejZFZY7TK)

***

### Step 6 — Establish a support channel and escalation path

Set up a government support layer between schools, installers, and the Giga team before the rollout begins.

**Support channels for schools**

Schools need a named channel to ask for help during and after installation. The right format depends on scale and infrastructure. Most deployments use a combination.

| Channel | Works best for | Notes |
|---|---|---|
| WhatsApp group | All strategies | Easy to set up, instant reach, works on mobile. Create one group per region for large rollouts. |
| Hotline / phone number | Expert in-person, Hybrid | Ideal when schools have low digital confidence. Assign a named person, not a generic number. |
| Email help desk | Guided remote, Self-installation | Allows written documentation of issues. Set a response time SLA (e.g. 48h). |
| Virtual drop-in sessions | Guided remote | Scheduled video sessions where schools can join with live questions. |
| Peer focal point network | Hybrid, Self-installation | Schools that installed successfully support nearby schools. Reduces load on central team. |

{% hint style="success" %}
Whichever channel you use, publicise it during the training workshop and include it in the installation guide you send to schools. Schools that can't find support simply give up.
{% endhint %}

**Escalation path**

Beyond the school-facing channel, establish a clear escalation path for issues that cannot be resolved at school level:

* A named government support owner (first escalation from installers)
* A basic troubleshooting runbook (common issues + first-response steps)
* A documented escalation path to Giga: who contacts whom, with what information

**Output:** Document the following and circulate to all installers before the rollout begins:

{% hint style="info" %}
**Support channel and escalation protocol**\
School support channel: \[channel type, contact details, response time]\
Government support owner: \[Name, phone / email]\
When to escalate to government support: \[e.g. issue not resolved by installer within 24h]\
Giga escalation contact: \[Name / email at UNICEF country office]\
When to escalate to Giga: \[e.g. issue unresolved at government level after 48h]\
Information to include when escalating: school name and ID, Giga Meter version, error message or screenshot, steps already attempted
{% endhint %}

→ [Rollout Monitoring — Escalation path](rollout-monitoring.md)

***

### Step 7 — Train installers

Run one or more training sessions (virtual or in-person) and keep a support channel open throughout the rollout (e.g. WhatsApp group, email list).

**Materials available from Giga:**

* Giga Meter Onboarding deck (EN / ES)
* Workshop Checklist (EN)
* Installation Guide (EN / ES / FR / PT / MN)
* Installation videos (subtitles in EN / PT / MN)

**Output:** Confirm the following before the first installation session:

{% hint style="info" %}
**Training plan**\
Training format: \[e.g. Zoom webinar / in-person workshop / regional sessions]\
Date(s):\
Materials language(s):\
Installer support channel: \[e.g. WhatsApp group name / help desk email]
{% endhint %}

→ [Workshop & School Checklist](deployment-checklist.md)

***

### Step 8 — Monitor the rollout

Track progress against your planned timeline and target from the day installation begins. Share monthly updates with the Giga team for the first three months, then quarterly.

**Three metrics to track from the start:**

| Metric                                                   | What it tells you                               |
| -------------------------------------------------------- | ----------------------------------------------- |
| % of target schools with Giga Meter installed            | Are you on pace?                                |
| % of installed schools reporting data in the last 7 days | Are installed schools actually collecting data? |
| Open troubleshooting tickets per week                    | Is the support mechanism keeping up?            |

**Output:** Share a monthly update with the Giga team using this format:

{% hint style="info" %}
**Monthly rollout update — \[Month, Year]**\
Target schools: \[N]\
Schools installed: \[N] (\[%])\
Schools reporting in the last 7 days: \[N] (\[%])\
Open troubleshooting tickets: \[N]\
Main blockers:\
Next steps:
{% endhint %}

→ [Rollout Monitoring](rollout-monitoring.md)

***

### Step 9 — Follow up with school-level focal points

Identify a responsible individual at each school to maintain the app. If a device is replaced or reformatted, Giga Meter must be reinstalled — school focal points are responsible for flagging this.

**Output:** Maintain a registry of school focal points, updated whenever contacts change.

| School name | School ID | Focal point name | Role | Phone / email |
| ----------- | --------- | ---------------- | ---- | ------------- |
|             |           |                  |      |               |

***

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

***

### Step 2 — Identify data users and assign access roles

Identify who in the ministry — and beyond — needs Giga Meter data and at what level. School-level focal points and regional coordinators may also require access.

**Output:** Share this list with the Giga team when requesting access provisioning.

| Name | Role | Unit | Access channel  | Notes                   |
| ---- | ---- | ---- | --------------- | ----------------------- |
|      |      |      | Dashboard / API | e.g. national view only |

→ [Access Channels: Dashboard and API](../data/access-channels.md)

***

### Step 3 — Onboard data users to their access channels

Each identified user should be able to locate their data — school, regional, or national view — and export it independently. For dashboard users, organise a guided walkthrough (live or recorded) covering filters, comparisons, and data export.

**Output:** Every user has logged in and can independently pull the data they need for their role.

→ [Using the Dashboard](../data/dashboard-guide.md)

***

### Step 4 — Establish metric literacy

Giga Meter reports several technical metrics. Circulate a simple reference explaining what each metric means and what a good or problematic result looks like in the country's context.

**Output:** Metric glossary circulated to all data users.

→ [Metric Glossary](../data/metric-glossary.md)

***

### Step 5 — Define KPIs

Translate the use case into 3–5 measurable KPIs, each with a formula, threshold, owner, and review frequency. Share the completed KPI document with the Giga data team so they can advise on whether the standard dashboard covers your needs or requires customisation.

**Output:** Share the completed KPI document with the Giga data team.

| KPI name | Formula | Threshold | Owner | Review cadence | Action triggered |
| -------- | ------- | --------- | ----- | -------------- | ---------------- |
|          |         |           |       |                |                  |

→ [Defining and Tracking KPIs](../data/kpi-guide.md)

***

### Step 6 — Set a KPI review and decision-triggering process

Define how often KPIs are reviewed, who runs the review, and what triggers action. Establish this process before the data starts flowing.

**Output:** Document and circulate the review process to all data users:

{% hint style="info" %}
**KPI review process**\
Meeting owner:\
Review cadence: \[weekly / monthly / quarterly]\
Format: \[e.g. standing meeting, shared dashboard, written brief]\
KPI | Threshold | Action triggered\
\[KPI name] | \[threshold] | \[action]
{% endhint %}

***

### Step 7 — Build capacity for ongoing analysis

Over time, government teams should be able to produce their own analyses: connectivity briefs, ISP performance reviews, and school-level investigations. If deeper analytical support is needed, contact the Giga data team.

**Output:** After 6–12 months, government users can produce and interpret analyses independently.

***

## All deployment resources

| Resource                                                         | What it's for                                               |
| ---------------------------------------------------------------- | ----------------------------------------------------------- |
| [Deployment Blueprint](deployment-blueprint.md)                  | Planning questionnaire — complete before the rollout starts |
| [Device Readiness Checklist](device-readiness.md)                | School-level device and connectivity check (Step 3)         |
| [Installation Strategies](installation-strategies.md)            | Four approaches and how to choose (Step 5)                  |
| [Workshop & School Checklist](deployment-checklist.md)           | Trainer guidance and school preparation materials (Step 7)  |
| [Rollout Monitoring](rollout-monitoring.md)                      | Health metrics, reporting cadence, escalation path (Step 8) |
| [Defining Your Use Case](../data/use-case-definition.md)         | How to frame what you're using the data for                 |
| [Access Channels: Dashboard and API](../data/access-channels.md) | Getting dashboard access and provisioning users             |
| [Using the Dashboard](../data/dashboard-guide.md)                | Screen-by-screen dashboard walkthrough                      |
| [Metric Glossary](../data/metric-glossary.md)                    | Definitions for every metric                                |
| [Defining and Tracking KPIs](../data/kpi-guide.md)               | KPI framework and templates                                 |
