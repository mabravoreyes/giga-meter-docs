# Defining Your Use Case

Before onboarding any user to the dashboard, decide what you are using Giga Meter for. This shapes which KPIs to track and which decisions the data is supposed to inform.

> [!IMPORTANT]
> Without a defined use case, dashboard users tend to look at the data without knowing what to do with it. The use case definition is the foundation of the entire data analysis workstream.

---

## What a use case defines

A use case answers three questions:

1. **What decision will this data inform?** (e.g., which schools to prioritise for ISP upgrades; whether a provider is meeting contract terms; whether a national connectivity target is on track)
2. **Who makes that decision?** (e.g., the MoE IT unit, the planning department, the minister)
3. **How often is that decision made?** (e.g., monthly for operational reviews, annually for budget planning)

---

## Country examples

| Country | Use case | Decision triggered |
|---|---|---|
| Brazil | National Connected Schools Strategy — target: 1 Mbps per student in the longest shift | Schools below the threshold are flagged for ISP renegotiation |
| Moldova (SVG) | ISP contract enforcement | If a school is unconnected for 3 consecutive working days, the ISP is fined |
| General | Deployment monitoring | Schools not reporting within 7 days get a follow-up call from the regional coordinator |

---

## Writing your use case

Aim for one paragraph or a short set of bullet points. It should answer:

- What is Giga Meter being used to monitor?
- What counts as a problem (threshold or condition)?
- Who acts on it, and what do they do?

**Example:**
> "We are using Giga Meter to monitor whether schools in the northern region are receiving the minimum contracted speed of 10 Mbps. Schools below this threshold for two consecutive weeks are reported to the regional ISP coordinator for follow-up. Reports are reviewed monthly by the MoE IT department."

Share this with the Giga team before the first dashboard onboarding session. It helps the team configure the dashboard filters and alerts most relevant to your context.

---

## Connecting use case to KPIs

Once the use case is clear, define the KPIs that operationalise it. See [Defining and Tracking KPIs](kpi-guide.md).

Common KPI types:

| Use case type | Typical KPIs |
|---|---|
| Policy enforcement | % schools meeting national speed benchmark; # schools below benchmark for 30+ consecutive days |
| ISP service monitoring | % schools where measured speed is within X% of contracted speed |
| Deployment tracking | % schools with active Giga Meter data; % reporting in the last 7 days |
| Baseline and trend analysis | Average download speed per district per quarter; YoY change in median latency |

---

## Related pages

- [KPI Guide](kpi-guide.md) — how to define and document your KPIs
- [Metric Glossary](metric-glossary.md) — definitions for every metric
- [Using the Dashboard](dashboard-guide.md) — how to pull data for your use case
- [Government Onboarding Overview](../deployment/government-onboarding-overview.md)
