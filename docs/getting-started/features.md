# Features

## Features

Giga Meter gives each connected school an automated, ongoing record of how its internet performs. Measurements feed into Giga Maps and analytics dashboards each day, with no action required at the school.

***

### Automated measurement

Giga Meter runs on its own once installed.

Four speed tests run each day: one within 15 minutes of the device starting up, then one in each of the 8am-12pm, 12pm-4pm, and 4pm-8pm windows. Test times are randomised within each window. Between speed tests, a ping check runs every 15 minutes from 8am to 8pm to record whether the connection is reachable.

No staff action is required once the app is installed.

{% hint style="info" %}
**Manual tests are also available.** Any user can start an on-demand test from the app at any time. This is useful during site visits or when investigating a reported issue.
{% endhint %}

***

### What gets measured

Every speed test records:

* **Download speed** - measured with M-Lab's NDT7 protocol against the nearest available M-Lab server
* **Upload speed** - same protocol and server
* **Latency** - minimum round-trip time (MinRTT) per test
* **Uptime** - derived from ping checks: the proportion of school hours (8am-8pm) during which the connection was confirmed reachable
* **ISP and network details** - ISP name, ASN, IP address, WiFi SSID, signal strength, channel, and adapter model

These measure the public internet connection, not the school's local network speed to the router.

***

### Tied to a school, not a device

Before the first measurement runs, the device is registered to a school using its national school ID. That registration links every later measurement to a school record in Giga's database, including the school's country, administrative divisions, education level, and environment type.

This enables three things:

**Geolocation validation.** Device coordinates are recorded on every test. If the device is more than 4km from the registered school's location, the measurement is flagged. This guards against data from misregistered or relocated devices.

**Multi-device coordination.** Up to three Giga Meter installations can be registered to the same school. Multiple devices measure independently, which makes the school's data more robust and reduces gaps when a device is offline.

**Persistent school history.** Because measurements are tied to a school ID rather than a device, the record survives device replacements. A school's connectivity history is preserved when hardware changes.

***

### Data where you need it

Every measurement syncs to Giga Maps and analytics dashboards automatically.

{% columns %}
{% column %}
**Giga Maps**

Results appear on the public Giga Maps platform within hours. Each school appears as a colour-coded dot showing its current connectivity level.
{% endcolumn %}

{% column %}
**Analytics dashboards**

Hosted dashboards (up to 10) show school-level and country-level trends: speeds over time, uptime by district, ISP performance, and comparison against national benchmarks.
{% endcolumn %}

{% column %}
**REST API**

Programmatic access to the full dataset - measurements, daily ping aggregations, school records, and country data - for integration with government systems or custom analysis.
{% endcolumn %}
{% endcolumns %}

***

### How Giga Meter compares to consumer speed tests

Consumer speed-test tools such as Ookla are user-initiated, anonymous, and built for individual awareness. Giga Meter is automated, registered to a school, and built for government reporting and accountability.

|                                    |                  **Giga Meter**                 | **Ookla / consumer apps** |
| ---------------------------------- | :---------------------------------------------: | :-----------------------: |
| Who initiates the test             |            Automated, fixed schedule            |            User           |
| Frequency                          |     4 speed tests + up to 48 ping checks/day    |         On demand         |
| Tied to a school record            |                       Yes                       |             No            |
| Geolocation validation             |         Yes, flagged if >4km from school        |             No            |
| School metadata                    | Country, admin levels, education level, Giga ID |             No            |
| Measures public internet (off-net) |                       Yes                       |            Yes            |
| Background operation               |            Yes, no user action needed           |             No            |
| Data goes to                       |         Giga Maps + government dashboard        |    Commercial platform    |
| Open source                        |                       Yes                       |             No            |

Every Giga Meter result is anchored to a school record, validated against a known location, and added to a shared evidence base that governments can use to hold ISPs accountable, plan investment, and track progress against connectivity targets.

***

→ Measurement protocols - detailed methodology\
→ Case studies - how governments use this data\
→ Pricing
