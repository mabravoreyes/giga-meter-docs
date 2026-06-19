# Defining and Tracking KPIs

Once your use case is defined, translate it into 3–5 measurable KPIs. Documented KPIs are what tell the Giga team whether the standard dashboard covers your needs or whether customisation is required.

---

## KPI structure

Each KPI should have:

| Field | Description |
|---|---|
| **Name** | Short, descriptive label |
| **Formula** | Exactly how the number is calculated |
| **Threshold** | What counts as "good" vs. "a problem" |
| **Owner** | Who is responsible for monitoring and acting on this KPI |
| **Review cadence** | How often the KPI is reviewed (weekly / monthly / quarterly) |
| **Action triggered** | What happens when the threshold is breached |

---

## KPI examples

### Policy enforcement

| | |
|---|---|
| **Name** | % schools meeting national speed benchmark |
| **Formula** | Schools with 30-day average download speed ≥ [national threshold] Mbps ÷ total schools with active Giga Meter × 100 |
| **Threshold** | ≥ 80% of schools above benchmark = on track; < 60% = escalate to ISP unit |
| **Owner** | MoE IT Department |
| **Review cadence** | Monthly |
| **Action triggered** | Schools below threshold for 30+ consecutive days are reported to the ISP coordinator for follow-up |

---

### ISP performance monitoring

| | |
|---|---|
| **Name** | % schools receiving contracted speed |
| **Formula** | Schools where measured speed ≥ 80% of contracted Mbps ÷ schools with known contract ÷ × 100 |
| **Threshold** | < 70% compliance = formal notice to ISP |
| **Owner** | Procurement / legal unit |
| **Review cadence** | Monthly |
| **Action triggered** | Formal notice to ISP; repeated failure triggers contract review |

---

### Deployment health

| | |
|---|---|
| **Name** | % installed schools actively reporting |
| **Formula** | Schools that sent ≥ 1 measurement in the last 7 days ÷ schools with Giga Meter installed × 100 |
| **Threshold** | < 70% = increase follow-up; < 50% = escalate to Giga |
| **Owner** | Installation lead |
| **Review cadence** | Weekly for first 3 months, then monthly |
| **Action triggered** | Contact silent schools; flag persistent drop-offs to Giga |

---

## Completing your KPI document

Fill in this table with your country's specific numbers and owners:

| KPI name | Formula | Threshold | Owner | Cadence | Action triggered |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

Share the completed KPI document with the Giga data team. If your KPIs require dashboard customisation (e.g., a column not yet in the standard view), the team will advise on feasibility and timeline.

---

## Reviewing KPIs

Define a regular review process before the data starts flowing:

- **Who runs the review?** Name a meeting owner — typically the Data Analysis Lead.
- **How often?** Weekly for the first month; monthly after the rollout stabilises.
- **What triggers action?** Specify the exact condition (threshold breach, sustained trend) that moves from "watch" to "act".
- **Where are decisions recorded?** A shared log, a ClickUp task, a brief — something that creates accountability.

Countries that define this process upfront are more likely to use Giga Meter data consistently over time. Countries that leave it informal tend to use the data reactively, only when a crisis prompts them.

---

## Related pages

- [Use Case Definition](use-case-definition.md)
- [Using the Dashboard](dashboard-guide.md)
- [Metric Glossary](metric-glossary.md)
- [Government Onboarding Overview](../deployment/government-onboarding-overview.md)
