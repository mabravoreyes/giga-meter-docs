# Government Onboarding Guide

Use this guide to plan and run a Giga Meter deployment, from initial setup through to sustained data use. Start here, then follow the dedicated guide for your role.

***

### Before you start

Two prerequisites must be in place before any installation can begin:

* [ ] **School data validated on** [**Giga Maps**](https://maps.giga.global/map) - the country's schools are mapped with official government IDs, and the data has been reviewed and approved by the government.
* [ ] **Country whitelisted on Giga's backend** - Giga enables the country in the system before Giga Meter can register schools. Email [gigatech@unicef.org](mailto:gigatech@unicef.org) to request whitelisting.

Contact your Giga focal point or UNICEF country office to confirm both are ready. Once confirmed, complete the [Deployment Blueprint](deployment-blueprint.md), a planning worksheet to align your team on strategy, scope, and timeline before the rollout begins.

***

### Two roles, running in parallel from day one

A Giga Meter deployment involves two workstreams. They can sit with the same department or person, but the activities are distinct and should run concurrently.

| Role                   | Responsible for                                                               | Typically held by                                           |
| ---------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Installation Lead**  | Getting Giga Meter running across schools and keeping it there                | MoE IT department, regional coordinators, school principals |
| **Data Analysis Lead** | Ensuring the data is used: defining use cases, onboarding users, setting KPIs | MoE planning or statistics unit                             |

Both workstreams start on day one. By the time the first schools report data, the data analysis side should already be ready to read it.

***

### Role 1 - Installation Lead

The Installation Lead coordinates the installer network, manages device readiness, runs training workshops, and monitors the rollout. Steps cover:

1. Designate the installation lead and subnational leads
2. Define target schools and phasing (pilot then scale-up)
3. Confirm device readiness across target schools
4. Ensure school IDs are known by installers
5. Choose an installation strategy (expert in-person / hybrid / guided remote / self-installation)
6. Establish a support channel and escalation path
7. Train installers
8. Monitor the rollout
9. Follow up with school-level focal points

**→** [**Installation Lead - Step-by-step guide**](installation-lead.md)

***

### Role 2 - Data Analysis Lead

The Data Analysis Lead ensures Giga Meter data feeds into government decisions, from defining the use case through to building analytical capacity over time. Steps cover:

1. Define the use case
2. Identify data users and assign access roles
3. Onboard data users to the [Superset Dashboard](https://superset.giga.global) or [API](https://maps.giga.global/docs/api/1)
4. Establish metric literacy
5. Define KPIs
6. Set a KPI review and decision-triggering process
7. Build capacity for ongoing analysis

**→** [**Data Analysis Lead - Step-by-step guide**](data-analysis-lead.md)

***

### Planning worksheet

Complete the [Deployment Blueprint](deployment-blueprint.md) before starting the rollout. It covers deployment rationale, installation planning, maintenance responsibilities, data use goals, and success metrics, and becomes your shared reference document with the Giga team.

***

### All deployment resources

| Resource                                                 | What it's for                                                       |
| -------------------------------------------------------- | ------------------------------------------------------------------- |
| [Deployment Blueprint](deployment-blueprint.md)          | Planning worksheet - complete before the rollout starts             |
| [Installation Lead Guide](installation-lead.md)          | Step-by-step guide for the Installation Lead                        |
| [Data Analysis Lead Guide](data-analysis-lead.md)        | Step-by-step guide for the Data Analysis Lead                       |
| [Training Support Materials](deployment-checklist.md)    | Session agenda, talking points, and Q\&A for installation workshops |
| [Case Studies](case-studies.md)                          | How other governments have used Giga Meter data                     |
| [Metric Glossary](../../installation/metric-glossary.md) | Definitions for every metric                                        |
| [API Reference](../technical-reference/api-reference.md) | Endpoint documentation for technical integrations                   |
