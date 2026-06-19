# Installation Lead — Step-by-step Guide

This guide is for the government official responsible for getting Giga Meter installed across schools and keeping it running. Work through these steps in order before and during the rollout.

← [Government Onboarding Guide](government-onboarding-overview.md)

---

## Step 1 — Designate the installation lead

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

## Step 2 — Define target schools and phasing

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

---

## Step 3 — Confirm device readiness

Before the rollout, verify that target schools meet the minimum device and connectivity conditions required for consistent data collection.

{% hint style="warning" %}
Giga Meter currently runs on Windows only. Tablets and Android devices cannot run the app. If a school has no Windows device, flag it to Giga before the rollout — Android support is in development.
{% endhint %}

For each school, confirm:

* [ ] **Windows OS** — Windows 7 or higher (desktop or laptop)
* [ ] **Free disk space** — at least 500 MB available
* [ ] **Regular use** — device is used daily or near-daily
* [ ] **Dedicated school connection** — device connects exclusively to the school's internet, not a mobile hotspot or personal router
* [ ] **Admin rights available** — the person installing can approve the installation
* [ ] **School internet connection** is functional and stable enough to complete an installation

Install on **at least two computers per school**. More devices mean more frequent measurements and redundancy if one device is switched off or reformatted.

**Common blockers**

| Blocker | What to do |
|---|---|
| School only has tablets or Chromebooks | Flag to Giga — Android support is in development |
| No Windows device available | Check if the school has any Windows computer in an office that stays on during school hours |
| Computers not regularly powered on | Discuss with school principal — measurements only run when the device is on and connected |
| No admin rights | Coordinate with MoE IT department to grant temporary admin access for installation |
| Internet connection down at time of visit | Reschedule or use a different device; note in the rollout tracker |

**Output:** Collect device status at the school level before the rollout and share with the Giga team.

| School name | School ID | Windows devices available | Powered on daily | Admin rights | Notes |
|---|---|---|---|---|---|
| | | | Yes / No | Yes / No | |

---

## Step 4 — Ensure school IDs are known by installers

Each school in Giga Meter is registered using an official school ID. Before the rollout, make sure the training covers what the school ID looks like in the country's system and where installers can look it up. Include a named support contact for cases where the school cannot be found or the ID appears incorrect.

**Output:** Include the following in installer training materials:

{% hint style="info" %}
**School ID reference**\
What the school ID looks like: \[e.g. format, example — "BR12345"]\
Where to find it: \[e.g. national school registry, MoE database, letter from the ministry]\
Support contact for ID issues: \[Name, phone / email]
{% endhint %}

---

## Step 5 — Choose an installation strategy

Choose how installations will happen based on country capacity, geography, school digital readiness, and scale. Four strategies have been used across Giga deployments — they can be combined.

{% tabs %}
{% tab title="Expert in-person" %}
<figure><img src="../../.gitbook/assets/strategy-expert-inperson.png" alt="Expert in-person installation" width="180"></figure>

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
<figure><img src="../../.gitbook/assets/strategy-hybrid.png" alt="Hybrid regional workshop installation" width="180"></figure>

**When to use:** Medium scale, with a regional structure. **Example: Sri Lanka.**

School IT staff attend regional training workshops and then carry out installation at their own school.

**Steps:**
1. Adapt and share the installation guide with school principals.
2. Ask schools to nominate 1–2 focal points responsible for installation and maintenance.
3. Organise in-person regional workshops — guide focal points live through the installation.
4. Set up a support channel (hotline or help desk) for post-workshop troubleshooting.
5. Monitor rollout and follow up with schools that fail to install.
{% endtab %}

{% tab title="Guided remote" %}
<figure><img src="../../.gitbook/assets/strategy-guided-remote.png" alt="Guided remote installation" width="180"></figure>

**When to use:** Larger scale, schools with decent IT capacity. **Example: Belize, Bosnia and Herzegovina.**

School focal points install Giga Meter themselves, supported through virtual training sessions and remote troubleshooting.

**Steps:**
1. Adapt and share the installation guide with school principals.
2. Ask schools to nominate 1–2 focal points responsible for installation and maintenance.
3. Organise virtual sessions — guide focal points live through the installation.
4. Set up a support channel (hotline or help desk) for post-session troubleshooting.
5. Monitor rollout and follow up with schools that fail to install.
{% endtab %}

{% tab title="Self-installation" %}
<figure><img src="../../.gitbook/assets/strategy-self-install.png" alt="Self-installation" width="180"></figure>

**When to use:** Large scale, schools with mature IT capacity. **Example: Botswana.**

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

---

## Step 6 — Establish a support channel and escalation path

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

---

## Step 7 — Train installers

Run one or more training sessions before the rollout and keep a support channel open throughout. See the [Training Support Materials](deployment-checklist.md) for a session agenda, talking points, and common Q&A.

**Materials available from Giga:**

* Giga Meter Onboarding deck (EN / ES)
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

→ [Training Support Materials](deployment-checklist.md)

---

## Step 8 — Monitor the rollout

Track progress against your planned timeline and target from the day installation begins. Share monthly updates with the Giga team for the first three months, then quarterly.

**Three metrics to track from the start:**

| Metric | What it tells you |
|---|---|
| % of target schools with Giga Meter installed | Are you on pace? |
| % of installed schools reporting data in the last 7 days | Are installed schools actually collecting data? |
| Open troubleshooting tickets per week | Is the support mechanism keeping up? |

{% hint style="success" %}
A school can be "installed" but not "reporting" — the device may be powered off, the app may have crashed, or it may have lost internet. Treat any installed school that hasn't reported in 7+ days as a priority follow-up.
{% endhint %}

Once schools start reporting, use the **Installation Tracking** tab in the Superset dashboard to monitor rollout health in real time. Key figures: live schools (data in last 21 days), at-risk schools (21–28 day silence), and drop-offs (28+ days silent).

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

---

## Step 9 — Follow up with school-level focal points

Identify a responsible individual at each school to maintain the app. If a device is replaced or reformatted, Giga Meter must be reinstalled — school focal points are responsible for flagging this.

**Output:** Maintain a registry of school focal points, updated whenever contacts change.

| School name | School ID | Focal point name | Role | Phone / email |
|---|---|---|---|---|
| | | | | |

---

## Related pages

* [Government Onboarding Guide](government-onboarding-overview.md)
* [Training Support Materials](deployment-checklist.md)
* [Installation Guide](../installation/installation-guide.md)
* [Using the Dashboard](../data/dashboard-guide.md)
