# Privacy & Security

Giga Meter is built and maintained by UNICEF's Giga Initiative. This page covers what data the app collects, how it is protected, and the governance frameworks that apply.

---

## Data policy

All Giga Meter measurement data is published under the [Open Database License (ODbL 1.0)](https://opendatacommons.org/licenses/odbl/). This license allows anyone to share, adapt, and build on the data as long as they attribute the source and keep any derived databases open.

The application is developed in accordance with [UNICEF's Privacy Policy](https://www.unicef.org/legal/privacy-policy). No personal data is collected. See [What data does Giga Meter transmit?](../troubleshooting/faq.md#what-data-does-giga-meter-transmit-to-giga) for the full field-level breakdown.

Data collected through M-Lab's NDT speed test infrastructure is additionally published as open data under M-Lab's [Open Database License (ODbL 1.0)](https://opendatacommons.org/licenses/odbl/) and is available in M-Lab's public BigQuery dataset. Anonymized test results (throughput, latency, server location, client IP subnet) are included. Giga's published dataset does not include raw IP addresses or test IDs that would link back to M-Lab's database.

---

## Infrastructure and hosting

All Giga products are hosted on **Microsoft Azure**, operating under Azure's shared responsibility model:

- **Microsoft is responsible for:** physical data centres, servers, and global networking infrastructure
- **Giga/UNICEF is responsible for:** application security, data, identities, and access controls

---

## Product security

| Area | Implementation |
|---|---|
| Transport encryption | All connections use TLS 1.2/1.3 (HTTPS and WebSocket over TLS). No plaintext connections. |
| Authentication | JWT (JSON Web Tokens) for all API requests. All requests are authenticated and logged. |
| Input validation | Defense against SQL injection, XSS, and data integrity threats |
| Data at rest | Encrypted using Azure-managed keys via Azure Blob Storage |
| Secrets management | Securely stored in App Service settings — not in code |
| Storage access | Public access to storage accounts is blocked |
| CORS policies | Restricted to authorised origins |
| Soft delete | Enabled for data recovery |
| Data retention | Active retention policy applied |
| Threat protection | Azure Defender enabled |

---

## Identity and access management

Access to Giga's backend systems follows least-privilege principles:

- **Role-Based Access Control (RBAC):** each team member has only the permissions their role requires
- **Authentication:** Microsoft Entra ID (formerly Azure AD) for single sign-on (SSO) and multi-factor authentication (MFA)
- **Access review:** regular reviews of access policies and permissions

---

## Development and deployment pipeline

| Stage | Tool / Practice |
|---|---|
| CI/CD | Azure DevOps and GitHub Actions with managed identities |
| Code quality | SonarQube static analysis and dependency checks |
| Environments | Isolated dev, staging, and production environments |
| Error tracking | Self-hosted Sentry instance (`excubo.unicef.io`) and Azure Monitor for real-time tracking |

---

## Monitoring and compliance

**Monitoring tools:** Azure Monitor, Log Analytics Workspace, and Azure Defender for Cloud provide:
- Threat detection (brute force, malware)
- Alerts and actionable insights
- Compliance monitoring via Azure Policy

**Governance frameworks:**
- Azure security best practices
- UNICEF Privacy Policy
- HTTPS enforcement across all endpoints
- Regular activity log reviews

---

## Speed test infrastructure (M-Lab)

Giga Meter uses [Measurement Lab (M-Lab)](https://www.measurementlab.net/) for speed tests — the same open-source infrastructure used by Google's internet speed test and other major measurement tools globally.

M-Lab operates a globally distributed fleet of servers. Giga Meter does not connect to a fixed server — it dynamically selects the nearest available server at the time of each test. M-Lab maintains several deployment tiers:

| Tier | Description |
|---|---|
| Cloud deployments | Cloud-hosted resources, managed by M-Lab |
| Full site deployments | Multiple co-located servers, managed by M-Lab |
| Minimal site deployments | Single server, managed by M-Lab |

For network whitelisting, a single DNS wildcard rule (`*.measurementlab.net`) covers all M-Lab servers regardless of tier. See [Network Destinations & Firewall Configuration](network-destinations.md) for the complete whitelist.

---

## Related pages

- [Network Destinations & Firewall Configuration](network-destinations.md)
- [Data Governance & Privacy](../technical-reference/data-governance.md)
- [FAQ — What data does Giga Meter transmit?](../troubleshooting/faq.md#what-data-does-giga-meter-transmit-to-giga)
- [Measurement Protocols](../technical-reference/measurement-protocols.md)
