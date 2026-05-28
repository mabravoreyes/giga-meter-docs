# Data Governance and Management

Giga Meter is designed to collect, store, and manage internet measurement data responsibly — ensuring transparency, privacy, and ethical data use. Data management practices adhere to [UNICEF's Privacy Policy](https://www.unicef.org/legal/privacy-policy) and industry best practices.

---

## What data is collected

### Measurement data

| Data point | Collected |
|---|---|
| Download speed | Yes |
| Upload speed | Yes |
| Latency | Yes |
| Ping / jitter | Yes |
| Uptime (ping-based) | Yes |

### Device and network metadata

| Data point | Collected |
|---|---|
| School IP address | Yes |
| School ID | Yes |
| App version | Yes |
| Operating system | Yes |
| Detected ISP | Yes |
| Network type | Yes |

### What is NOT collected

| Data type | Collected |
|---|---|
| Personally identifiable information (PII) | **No** |
| Activity logs | **No** |
| Browsing data | **No** |
| Personal files or content | **No** |
| Internet usage content | **No** |

---

## Data storage and security

Data is securely stored in compliance with best practices in data management, leveraging **Microsoft Azure's security framework**.

The application does not collect or store activity logs, browsing data, or any information about internet usage at the school.

---

## Data accessibility and use

A subset of the data collected via Giga Meter is made publicly available as open connectivity data:

**Public data includes:**
- Test results: download speed, upload speed, latency, uptime
- A unique Giga-created school identifier

This data is made available under the **[CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode.en)**, making it freely available for reuse and redistribution.

**How to access:**
- **Giga Maps:** [maps.giga.global/map](https://maps.giga.global/map) — search for your school to view results over time
- **API:** [maps.giga.global/docs/explore-api](https://maps.giga.global/docs/explore-api) — bulk access and further analysis

---

> [!NOTE]
> The data collected by Giga Meter will be shared with the public in combination with information about the registered school. No personal data is ever shared.
