# Case Studies

How governments are using Giga Meter data to drive decisions. Each deployment below started with a defined use case — a specific decision the data was meant to inform.

← [Government Onboarding Guide](government-onboarding-overview.md)

---

## Countries at a glance

| Country | Main goal | Benchmark | Deployment model |
|---|---|---|---|
| Brazil | Enforce school-specific speed targets and validate ISP fiscal obligations | 1 Mbps per enrolled student in the longest shift | Hybrid |
| Botswana | Track compliance against national connectivity mandate | 100 Mbps | Remote (centralised support team) |
| Mongolia | Improve LAN performance; enable decentralised ISP contracting | No formal minimum | Remote (centralised support team) |
| Malawi | Verify ISP-reported vs. student-experienced speeds | ISP contractual commitments | — |
| Fiji | Identify schools reliable enough for live broadcast STEM lessons | No formal minimum | Hybrid |
| Bosnia and Herzegovina | Identify schools meeting criteria for digital education programming | Meaningful connectivity | Hybrid |
| Sri Lanka | Establish national connectivity baseline, starting in Eastern Province | No formal minimum | Hybrid (province-level trainings) |
| Namibia | Generate evidence for procurement decisions | 100% of schools at 1 Gbps by 2030 | Hybrid |

---

## Policy enforcement

### Brazil — Speed benchmark compliance and outcome-based ISP funding

**Context:** Brazil's *Estratégia Nacional de Escolas Conectadas* (ENEC) sets a target of 1 Mbps per enrolled student in the longest school shift. With hundreds of thousands of schools, manual compliance verification is not feasible.

**Use case:** Real-time Giga Meter data allows the Ministry of Communications (MCom) to monitor which schools meet the benchmark continuously — not just at contract signing. The same data validates ISP performance under the FUST Fiscal Benefit, which allows ISPs to fulfil their Universal Service Fund obligations by delivering measured high-speed connectivity to schools rather than paying into a central fund.

**Decision triggered:** Schools below the per-student threshold are flagged for ISP follow-up. ISP fiscal benefit claims are only accepted when validated against live measurement data.

**What makes this model work:** The benchmark is school-specific (it scales with enrolment), not a fixed Mbps number. This makes it harder for ISPs to meet the letter of the contract while underserving larger schools.

---

### Botswana — Village Connectivity Project monitoring

**Context:** Botswana's Village Connectivity Project aims to connect schools to a 100 Mbps standard. With ~700 schools connected, the government needed a way to verify that the standard was being met in practice, not just on paper.

**Use case:** Giga Meter data is integrated into the government's SmartBots monitoring initiative. Schools are assessed against the 100 Mbps benchmark on an ongoing basis. The same model is being extended to health centres and community facilities, with school connectivity infrastructure shared across sectors to improve affordability.

**Deployment model:** Remote, centralised support team — schools install Giga Meter independently following the installation guide, with a government-run support desk for troubleshooting.

**Decision triggered:** Schools consistently below 100 Mbps are identified for ISP renegotiation or infrastructure upgrade planning.

---

### Mongolia — LAN triangulation and decentralised ISP contracting

**Context:** Mongolia's Education Information Technology Centre (EITC) monitors internet performance in schools via LibreNMS on routers and access points alongside Giga Meter on user devices. The data is triangulated to identify whether connectivity problems sit at the ISP level, the router, or the local access point.

**Use case:** Giga Meter provides the end-device measurement layer that the infrastructure-side tools (LibreNMS) cannot. Together, the data is used to troubleshoot and improve quality of experience for end users — students and teachers.

Mongolia is also moving to decentralised connectivity contracting, allowing schools to contract ISPs directly within standardised Service Level Agreements. Giga Meter data provides the evidence base for schools and regional coordinators to hold ISPs accountable at the contract level.

**Decision triggered:** Schools with poor end-device performance despite healthy router metrics are flagged for ISP-side investigation. Contract renewal decisions are informed by school-level measurement history.

---

## ISP accountability

### Malawi — Closing the gap between reported and experienced speeds

**Context:** ISPs in Malawi report connectivity performance under their contracts. Governments had no independent way to verify whether what ISPs reported matched what students actually experienced.

**Use case:** Giga Meter provides an independent, standardised baseline of student-experienced connectivity — measured at the device level, not at the ISP handoff point. The pilot used this data to:

- Establish a credible baseline of real-world connectivity (not ISP-reported)
- Diagnose which schools underperformed due to ISP factors vs. local infrastructure or congestion
- Give governments reproducible evidence to assess ISP contract adherence at scale

**Decision triggered:** Evidence base for government accountability proceedings with ISPs. Specific schools with persistent underperformance can be cited with documented measurement history.

---

## Digital education programming

### Fiji — Identifying schools ready for live STEM broadcast lessons

**Context:** Fiji faces a shortage of qualified STEM teachers in its remote island communities. The Ministry of Education developed a programme to broadcast live STEM lessons to multiple schools simultaneously — but this only works for schools with reliable, stable connectivity.

**Use case:** Giga Meter data is used to identify which schools have connectivity stable enough to support live broadcast lessons. A school that frequently drops or shows high variability cannot reliably participate. The data makes the selection process evidence-based rather than relying on school self-reporting or ISP claims.

**Decision triggered:** Only schools with confirmed reliable connectivity over a monitoring period are enrolled in the live lesson programme. Schools that fall below threshold are flagged for infrastructure support before enrolment.

---

### Bosnia and Herzegovina — Meaningful connectivity screening

**Context:** A digital education programme needed to identify which schools met a "meaningful connectivity" threshold before deploying content and devices.

**Use case:** Giga Meter data was used to screen schools against the meaningful connectivity benchmark — a composite threshold that considers download speed, upload speed, latency, and uptime together. Schools not meeting the benchmark were excluded from the initial programme cohort and flagged for connectivity support.

**Decision triggered:** School eligibility for digital education programme enrolment. Schools below threshold routed to a separate infrastructure support workstream.

---

## Baseline and planning

### Sri Lanka — Provincial baseline before national rollout

**Context:** Sri Lanka had no standardised, independently verified baseline of school connectivity. National expansion of digital education programming required knowing the real state of connectivity — not survey responses or ISP records.

**Use case:** Giga Meter was deployed in a phased hybrid rollout, beginning with Eastern Province schools trained through regional workshops. Data from the province provided the first reliable, school-level connectivity baseline to inform national planning.

**Decision triggered:** Baseline data used to identify which schools can support digital programming and which require investment before rollout.

---

## Procurement and investment

### Namibia — Evidence for connectivity procurement

**Context:** Namibia's national target is 100% of schools connected at 1 Gbps by 2030. Before negotiating large-scale connectivity contracts, the government needed verified data on current performance to anchor procurement discussions.

**Use case:** Giga Meter provides independent, school-level performance data that governments can use in procurement negotiations — replacing ISP-reported figures with independently verified measurements.

**Decision triggered:** Procurement team enters negotiations with verified performance baselines, gap analysis by region, and historical trend data.

---

## Starting your own use case

Every deployment above started with a simple definition: what decision will this data inform, who makes it, and how often?

→ [Data Analysis Lead Guide — Step 1](data-analysis-lead.md)

Use the table at the top of this page as a reference when completing your own use case definition. If your country's goal matches one of the types above, adapt the corresponding case study as a starting template.
