# Privacy & Security

Giga Meter is built and maintained by UNICEF's Giga initiative. This page describes what data the app collects, how it is protected, and the governance frameworks that apply.

**In short:** Giga Meter collects only technical connectivity measurements. It does not collect personal data, student information, or school staff records. All measurement data is published as open data under a standard international license.

***

### Data collected

Giga Meter measures the quality of a school's internet connection. The data it collects is entirely technical:

* Download and upload speed, latency, and packet loss
* The internet service provider (ISP) and network type
* Device type and Giga Meter app version
* Test timestamp and test server location

It collects no names, no student records, no staff information, and no location data beyond what is needed to identify the ISP. See [What data does Giga Meter transmit?](../troubleshooting/faq.md) for the complete field-level list.

***

### Data license

All Giga Meter measurement data is published under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license. This means:

* Anyone can access, share, and use the data
* Anyone can build tools or reports on top of it
* The only requirement is that the source (Giga/UNICEF) is credited

The application is developed in accordance with [UNICEF's Privacy Policy](https://www.unicef.org/legal/privacy-policy).

***

### Where data is stored

All Giga products are hosted on **Microsoft Azure**, a cloud platform operated by Microsoft and used by governments, international organisations, and enterprises worldwide. Azure is compliant with ISO 27001, SOC 2, and other international standards.

Under Azure's shared responsibility model:

* **Microsoft** is responsible for physical data centres, servers, and network infrastructure
* **Giga/UNICEF** is responsible for application security, data governance, and access controls

***

### How data is protected

| Protection measure   | What it means in practice                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Encrypted in transit | All data sent between the app and Giga's servers is encrypted. No data travels in plaintext.                      |
| Encrypted at rest    | Stored data is encrypted on Giga's servers. Unauthorised parties cannot read it even with physical server access. |
| Access controls      | Only authorised Giga and UNICEF staff can access backend systems. Access is role-based and regularly reviewed.    |
| Authentication       | All API access requires a verified token. Unauthenticated requests are rejected.                                  |
| Input validation     | The app is protected against common web security threats (injection attacks, data manipulation).                  |
| Secrets management   | Credentials and configuration keys are stored securely, not in the application code.                              |
| Threat protection    | Microsoft Azure's security monitoring detects and alerts on suspicious activity.                                  |
| Soft delete          | Data deletion is reversible, preventing accidental permanent loss.                                                |

***

### Who can access your country's data

Access to country-level data on the Superset dashboard follows a role-based model:

* Users create an account at [superset.giga.global](https://superset.giga.global)
* The Giga team assigns a country-specific role, so users can only see data for the countries they are authorised for
* No user can view data from another country without explicit authorisation

For API access, the same principle applies: API keys are scoped to specific countries and must be requested through the Giga team.

***

### Single sign-on and multi-factor authentication

Giga's internal team accesses backend systems via Microsoft Entra ID (formerly Azure AD), which provides:

* **Single sign-on (SSO):** staff use one set of credentials across all Giga systems
* **Multi-factor authentication (MFA):** login requires both a password and a second verification step
* **Centralised access management:** when a team member leaves or changes role, access is removed centrally

***

### Development practices

Giga Meter is developed and released through a managed pipeline:

* Code is reviewed and tested before it reaches production
* Static analysis tools check for common security vulnerabilities before each release
* Development, staging, and production environments are kept separate, so changes are tested before users see them
* Application errors are monitored through a self-hosted error tracking system operated by UNICEF

***

### Speed test infrastructure

Giga Meter uses [Measurement Lab (M-Lab)](https://www.measurementlab.net/) to run speed tests, the same infrastructure used by Google's speed test and other widely used measurement tools. M-Lab is an open-source project supported by academic and technology partners globally.

M-Lab operates a globally distributed network of servers. Giga Meter selects the nearest available server for each test; no fixed server is used.

For network whitelisting, a single DNS wildcard rule (`*.measurementlab.net`) covers all M-Lab servers. See [Network Destinations & Firewall Configuration](../../technical-reference/network-destinations.md) for the complete list.

***

### Related pages

* [Network Destinations & Firewall Configuration](../../technical-reference/network-destinations.md)
* [Data Governance & Privacy](../technical-reference/data-governance.md)
* [FAQ - What data does Giga Meter transmit?](../troubleshooting/faq.md)
* [Measurement Protocols](../technical-reference/measurement-protocols.md)
