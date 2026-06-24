# What Giga Meter does

Governments can't improve what they can't measure. Giga Meter gives every connected school a permanent, automated record of how its internet actually performs — feeding data directly into Giga Maps and your own analytics dashboards, day after day, without anyone at the school having to do anything.

***

## Automated measurement

Install once. After that, Giga Meter runs on its own.

Four speed tests run every day — one within 15 minutes of the device starting up, then one in each of the 8am–12pm, 12pm–4pm, and 4pm–8pm windows. Test times are randomised within each window to avoid patterns. Between speed tests, ping checks run every 15 minutes from 8am to 8pm to track whether the connection is up at all.

No button to press. No staff action required. No risk of tests being forgotten.

{% hint style="info" %}
**Manual tests are available too.** Any user can trigger an on-demand test from the app interface at any time — useful during site visits or when troubleshooting a reported issue.
{% endhint %}

***

## What gets measured

Every speed test captures:

* **Download speed** — measured via M-Lab's NDT7 protocol against the nearest available M-Lab server
* **Upload speed** — same protocol, same server
* **Latency** — minimum round-trip time (MinRTT) per test
* **Uptime** — derived from ping checks: the proportion of school hours (8am–8pm) during which the connection was confirmed reachable
* **ISP and network details** — ISP name, ASN, IP address, WiFi SSID, signal strength, channel, and adapter model on every test

These are measurements of the **public internet connection** — not the school's local network speed to the router.

***

## Tied to a school, not a device

This is what makes Giga Meter different from a speed test app.

Before the first measurement runs, the device is registered to a specific school using its national school ID. That registration links every subsequent measurement to a school record in Giga's database — including the school's country, administrative divisions, education level, and environment type.

A few things this makes possible:

**Geolocation validation.** Device coordinates are captured on every test. If the device running Giga Meter is more than 4km from the registered school's location, the measurement is automatically flagged. This prevents data quality issues from misregistered devices or devices moved off-site.

**Multi-device coordination.** Up to 3 Giga Meter installations can be registered to the same school. Multiple devices measure independently, making the school's data more robust and reducing gaps from device downtime.

**Persistent school history.** Because measurements are tied to a school ID rather than a device, the historical record survives device replacements. A school's connectivity trend is preserved even when hardware changes.

***

## Data where you need it

Every measurement syncs to Giga Maps and your analytics dashboards automatically — no manual exports, no CSV files.

{% columns %}
{% column %}
**Giga Maps**

Results appear on the public Giga Maps platform within hours. Schools appear as colour-coded dots showing their current connectivity level. Governments, partners, and school staff can see the data directly.
{% endcolumn %}

{% column %}
**Analytics dashboards**

Hosted dashboards (up to 10) show school-level and country-level trends: speeds over time, uptime by district, ISP performance, and benchmark comparison against national targets.
{% endcolumn %}

{% column %}
**REST API**

Programmatic access to the full measurement dataset — measurements, daily ping aggregations, school records, and country data — for integration with government systems or custom analysis.
{% endcolumn %}
{% endcolumns %}

***

## How is Giga Meter different from Ookla?

Consumer speed test apps give you a number. Giga Meter gives you a record.

The difference is structural: Ookla and similar tools are user-initiated, anonymous, and built for personal awareness. Giga Meter is automated, school-registered, and built for government accountability.

|  | **Giga Meter** | **Ookla / consumer apps** |
| --- | :---: | :---: |
| Who initiates the test | Automated — fixed schedule | User |
| Frequency | 4 speed tests + up to 96 ping checks / day | On demand |
| Tied to a school record | ✓ | — |
| Geolocation validation | ✓ Flagged if >4km from school | — |
| School metadata | Country, admin levels, education level, Giga ID | — |
| Measures public internet (off-net) | ✓ | ✓ |
| Background operation | ✓ No user action needed | — |
| Data goes to | Giga Maps + government dashboard | Commercial platform |
| Open source | ✓ | — |

The right framing: Giga Meter treats **the school** as the unit of measurement. Every result is anchored to a school record, validated against a known location, and contributed to a shared evidence base that governments can use to hold ISPs accountable, plan investments, and track progress against connectivity targets.

***

→ [Measurement protocols — detailed methodology](../technical-reference/measurement-protocols.md)\
→ [Case studies — how governments use this data](case-studies.md)\
→ [Pricing](../pricing/pricing.md)
