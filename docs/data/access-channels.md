# Access Channels: Dashboard and API

Giga Meter data is accessible through two channels. Which one to use depends on how your team works with data.

---

## Overview

| Channel | Best for | Access |
|---|---|---|
| **Superset Dashboard** | Policy teams, ministry staff, country coordinators — people who need charts and tables without writing code | Login credentials provisioned by Giga |
| **API** | Technical teams, data analysts, partners who want to integrate Giga data into their own systems or run custom analyses | API key provisioned by Giga |

Both channels access the same underlying data. The difference is presentation and flexibility.

---

## Superset Dashboard

The dashboard provides seven pre-built screens covering:

- School-level summary (how many schools, headline speeds)
- Speed and latency trends over time
- District-level breakdowns
- Per-school and per-measurement data tables
- App version tracking and installation health

See [Using the Dashboard](dashboard-guide.md) for a screen-by-screen walkthrough.

**Getting access:**
Contact your Giga focal point or the UNICEF country office. They will provision login credentials for each user who needs dashboard access. When requesting access, provide the name, role, and email of each user.

**What each user can do:**
- Filter by school, district, date range, education level
- Export data from any table to CSV
- View time series, box plots, and distribution charts
- Share direct links to specific dashboard views

**What users cannot do:**
- Edit the dashboard or charts (read-only access)
- Access data from other countries

---

## API

The Giga Maps API provides programmatic access to school connectivity data. It is designed for technical users who want to:

- Pull data into their own analysis tools (Python, R, Excel via Power Query)
- Build automated reports or monitoring systems
- Integrate Giga data into government systems or dashboards

**Getting access:**
Contact the Giga team through your UNICEF country focal point to request an API key and documentation.

**What the API provides:**
- School-level measurements (download speed, upload speed, latency, uptime)
- School metadata (location, education level, government ID)
- Time-series data queryable by school, district, date range
- Data licensed under CC BY 4.0

---

## Identifying data users

Before requesting access, list who in the ministry (and beyond) needs Giga Meter data and what level of access they need. This is [Step 2 of the Data Analysis workstream](../deployment/government-onboarding-overview.md).

A simple format:

| Name | Role | Unit | Channel | Access level |
|---|---|---|---|---|
| [Name] | Planning Director | MoE Strategy Unit | Dashboard | National view |
| [Name] | IT Coordinator | MoE IT Department | Dashboard + API | All schools |
| [Name] | Regional Coordinator | [Region] Education Office | Dashboard | Regional filter only |

Share this list with the Giga team when requesting access provisioning.

---

## Related pages

- [Using the Dashboard](dashboard-guide.md)
- [Data Governance & Privacy](../technical-reference/data-governance.md)
- [Use Case Definition](use-case-definition.md)
- [Government Onboarding Overview](../deployment/government-onboarding-overview.md)
