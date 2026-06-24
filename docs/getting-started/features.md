# Features

Giga Meter is a desktop application that runs automated internet quality tests on school devices and streams results to Giga Maps — building a continuous, independently verified record of connectivity at every registered school.

***

## Measurement

{% columns %}
{% column %}
### Speed

Download and upload speeds measured via M-Lab's Network Diagnostic Tool (NDT7) protocol. Tests run against the nearest available M-Lab server, measuring the connection to the public internet — not local network speed to the router.
{% endcolumn %}

{% column %}
### Latency & uptime

Minimum round-trip time (MinRTT) captured on every speed test. Ping checks run every 15 minutes during school hours (8am–8pm local time) to track whether the connection is reachable. Daily uptime is derived from these checks.
{% endcolumn %}

{% column %}
### Network metadata

Every test captures the ISP name, ASN, IP address, hostname, WiFi SSID, signal strength, channel, and adapter model. This makes it possible to diagnose whether performance issues sit at the ISP level or the local network.
{% endcolumn %}
{% endcolumns %}

***

## Automated testing

Giga Meter runs on a fixed schedule — no action required from school staff once installed.

| | Detail |
| --- | --- |
| **Daily speed tests** | 4 per day: within 15 min of device startup, then one each in the 8am–12pm, 12pm–4pm, and 4pm–8pm windows |
| **Ping checks** | Every 15 minutes between 8am and 8pm local time |
| **Manual tests** | Available on demand from the app interface |
| **Scheduling** | Test times are randomised within each window to avoid patterns |
| **Background operation** | Tests run silently without interrupting device use |

***

## School identification

Every measurement is tied to a specific school — not just a device or IP address.

| Feature | Detail |
| --- | --- |
| **School registration** | Device is registered to a school using the national school ID, looked up in Giga's school database at setup |
| **Giga school ID** | Each school carries a persistent Giga ID that links measurements across devices and over time |
| **Geolocation validation** | Device coordinates are captured on every test. Measurements are automatically flagged if the device is more than 4km from the registered school location, or if GPS accuracy falls below 500m |
| **Multi-device support** | Up to 3 app instances can be registered per school. Multiple devices produce independent measurements and improve data reliability |
| **School metadata** | Measurements are tagged with country, admin1–admin4 divisions, education level, environment type, and ISP from the Giga school master |

***

## Data pipeline

| Feature | Detail |
| --- | --- |
| **Sync to Giga Maps** | Measurements sync every 4 hours; school registration syncs every hour |
| **REST API** | Authenticated API access to measurements, ping aggregation, school data, country data, and IP metadata |
| **Filtering and pagination** | All endpoints support pagination and filtering by school, country, date, and more |
| **Historical records** | Full measurement history retained; daily ping aggregations computed automatically |
| **Anomaly detection** | Schools can be flagged for data quality issues or anomalous measurements by administrators |

***

## Analytics dashboards

Included with Tier 1 and Tier 2 subscriptions. Hosted and maintained by Giga.

* School-level and country-level connectivity views
* Download speed, upload speed, latency, and uptime over time
* ISP-level performance breakdowns
* Benchmark comparison against national connectivity targets
* Up to 10 dashboards per deployment
* Custom dashboard development available at cost

***

## How is Giga Meter different from Ookla or other speed test apps?

Consumer speed test apps measure network performance as a one-off, user-initiated check. Giga Meter is built for continuous, unattended monitoring tied to a specific school — with data flowing into a shared public platform designed for government decision-making, not a consumer profile.

|  | **Giga Meter** | **Ookla / consumer apps** |
| --- | :---: | :---: |
| Measurement target | Public internet (off-net, via M-Lab) | Public internet |
| Who initiates the test | Automated — runs on fixed schedule | User-initiated |
| Frequency | 4 speed tests + up to 96 ping checks per day | On demand |
| Tied to a specific school | ✓ Registered to a school ID | — |
| Geolocation validation | ✓ Flagged if >4km from registered school | — |
| School metadata | Country, admin hierarchy, education level, Giga ID | — |
| Data destination | Giga Maps (public) + government dashboard | Commercial platform / user profile |
| Data ownership | UNICEF / government | Commercial operator |
| Multi-device coordination | Up to 3 devices per school | Independent sessions |
| Background operation | ✓ Runs without user action | — |
| Open source | ✓ | — |

The core difference: Giga Meter treats **the school** as the unit of measurement, not the device or the user. Every result is anchored to a school record, validated against a known location, and fed into a shared evidence base designed for policy and accountability — not a personal speed report.

***

→ [Measurement protocols](../technical-reference/measurement-protocols.md)\
→ [Pricing](../pricing/pricing.md)\
→ [Installation guide](../installation/installation-guide.md)
