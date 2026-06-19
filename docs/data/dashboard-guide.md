# Using the Dashboard

Giga's school connectivity dashboards are built in Apache Superset. This guide walks through each screen, explains what it shows, and maps the column names to their plain-language definitions.

{% hint style="info" %}
Dashboard access is provisioned by Giga. If you don't have login credentials, contact your Giga country focal point or the UNICEF country office.
{% endhint %}

---

## Dashboard overview

The dashboard has seven screens, accessible from the tab bar at the top. Each tab shows a different angle on the same underlying data.

| Screen | What it answers |
|---|---|
| **Summary** | How many schools are on the map, how many report through Giga Meter, and headline speed and latency figures |
| **Connectivity · Speed & Latency** | Daily speed and latency trends, and how speeds are distributed across schools |
| **Connectivity · District** | Average speed broken out by district, plus a per-school table with sparklines |
| **Data Tables · Registered** | One row per registered school — key operational fields for follow-up |
| **Data Tables · Measurements** | One row per individual test, including Wi-Fi diagnostics captured at measurement time |
| **App Tracking** | Which Giga Meter version is running across the country; daily reporting counts |
| **Installation Tracking** | Who's live, who's gone quiet, and drop-off rate by district |

---

## Screen 1 — Summary

The opening view. Two big numbers — how many schools are on the map and how many already report through Giga Meter — followed by headline speed and latency figures.

**Key fields on this screen:**

| What you see | Term | What it means |
|---|---|---|
| Black navigation bar | Superset | Standard Apache Superset chrome — Dashboards · Charts · Datasets · SQL |
| Left filter rail | School ID / Region / Time window | Narrow results by School ID, Education Level, Admin region, Giga ID, or date range |
| Schools on Giga Maps (e.g. 1.19k) | [Giga Maps](../technical-reference/measurement-protocols.md) | Schools that have been located and published on Giga Maps |
| Schools with Giga Meter (e.g. 81) | Giga Meter | Of the mapped schools, how many run the Giga Meter app and stream measurements |
| Small wave under the count | Time series | Daily count of Giga Meter schools — climbing means new rollouts |
| Connected / Not connected | Connectivity status | Schools with confirmed internet vs. no internet, based on all available sources |
| Live (e.g. 75) | Live school | Schools that sent a reading within the last 21 days |
| Drop-off (e.g. 5) | Drop-off | Schools silent for 28+ days — unlikely to come back without a site visit |
| At-risk (e.g. 1) | At-risk school | Schools in the 21–28-day quiet window |
| Average download (e.g. 85.59 Mbps) | Download speed | Average across all schools and all measurements in scope |
| Average upload (e.g. 75.43 Mbps) | Upload speed | Average upload — close to download means symmetric links |
| Average latency (e.g. 59 ms) | Latency | About the upper edge of what feels instant in a video call |
| Total measurements (e.g. 32.4k) | Measurement | Individual Giga Meter tests across all schools in the selected time window |

---

## Screen 2 — Connectivity · Speed & Latency

Daily speed and latency trends, plus box-plot distributions that show how consistent the experience is across schools.

**Key fields:**

| What you see | Term | What it means |
|---|---|---|
| Black line | Download speed | Average daily download, in Mbps |
| Blue line | Upload speed | Average daily upload — usually below download |
| Hover tooltip | Rolling average | Each point is the average of all measurements that day |
| Blue brush strip | Time series | Drag the handles to zoom into a date range |
| Box plot (right) | Speed distribution | Shaded box = middle 50% of schools; dots = outliers |
| Lower time-series chart | Latency | Average daily latency in milliseconds |
| Dot cloud (bottom right) | Distribution (statistical) | Latency spread — a long tail of very-high values usually means timeouts |
| Y-axis unit | Milliseconds (ms) | Under 50 ms is comfortable for video calls; over 200 ms causes noticeable lag |

---

## Screen 3 — Connectivity · District

Average speed broken out by the country's administrative districts, then a per-school table with a sparkline for each school.

**Key fields:**

| What you see | Term | What it means |
|---|---|---|
| Grey bars | Download speed | Average download per district |
| Green bars | Upload speed | Matching upload — side-by-side makes lag easy to spot |
| Tallest bar | Bandwidth | Higher means better-served schools in that district |
| Y-axis | Mbps (megabits per second) | 1 Mbps ≈ smooth audio call; 5 Mbps ≈ a class on HD video |
| "Last value" column | Load speed | The most recent single Giga Meter test reading |
| "Weekly Avg" column | Rolling average | Average of every measurement from the last seven days |
| "WoW %" column | Week-over-Week (WoW) % | −91% means this week's average is 91% lower than last week — worth investigating. "null" = not enough history |

---

## Screen 4 — Data Tables · Registered

One row per school that has registered through Giga Meter, with the operational fields most useful for follow-up.

**Key columns:**

| Column name | Term | What it means |
|---|---|---|
| `school_id_govt` | School ID (government) | The country's official school identifier (e.g. si00000104) — different from Giga's internal ID |
| `num_measurements` | Measurement | Total Giga Meter tests the school has ever run |
| Days since last measurement (green column) | Days since last measurement | 0 = sent a reading today; non-zero is an early warning |
| `num_devices_registered` | Number of devices registered | How many computers at the school are linked to Giga Meter |
| `most_recent_app_version` | App version | Newest Giga Meter build any device at the school is running |

{% hint style="success" %}
Sort by "days since last measurement" descending to surface schools that need follow-up first.
{% endhint %}

---

## Screen 5 — Data Tables · Measurements

One row per individual Giga Meter test. Includes the Wi-Fi diagnostics captured at the moment the test ran — useful for diagnosing whether a speed problem is an ISP issue or a local Wi-Fi issue.

**Key columns:**

| Column name | Term | What it means |
|---|---|---|
| `load_speed` | Load speed | Download speed recorded by this specific test, in Mbps |
| `isp_asn_clean` | ASN (Autonomous System Number) | Identifies which provider's network served this test (e.g. AS8926 = Moldtelecom) |
| `app_version` | App version | Which Giga Meter build ran this test |
| `avg_latency` | Latency | Latency recorded by this specific test, in ms |
| `isp_clean` | ISP | Carrier's human-readable name, cleaned from what the app captured |
| `detected_wifi_ssid` | SSID | Name of the Wi-Fi network the device was on during the test |
| Wi-Fi signal column | Wi-Fi signal | Signal strength in dBm — closer to zero is stronger (−60 is healthy; −85 is weak) |
| Wi-Fi quality column | Wi-Fi quality | Composite score combining signal strength and interference |
| Wi-Fi TX rate column | Wi-Fi TX rate | Data rate to the router in Mbps — drops as wireless link weakens |
| `detected_wifi_frequency` | Wi-Fi frequency | ~2400 = 2.4 GHz band; ~5000 = 5 GHz band |

{% hint style="info" %}
If a school shows low `load_speed` but a healthy `avg_latency` and strong Wi-Fi signal, the bottleneck is likely on the ISP side, not the school's internal network.
{% endhint %}

---

## Screen 6 — App Tracking

Shows which version of Giga Meter is deployed across the country and how many schools send data each day.

**Key elements:**

| What you see | Term | What it means |
|---|---|---|
| Donut chart | App version | Each wedge = a different Giga Meter build. A single wedge = uniform version across all schools |
| Bar chart | Real-time (RT) data | Each bar = number of schools that sent at least one measurement that day |
| Grey line | Rolling average | 7-day rolling count — smooths weekend dips and reveals growth trend |

{% hint style="success" %}
After a version update, watch this screen for schools still on older builds. A fragmented donut is an indicator that some devices missed the update.
{% endhint %}

---

## Screen 7 — Installation Tracking

Health-check view. Shows who's live, who's gone quiet, and how the drop-off rate breaks down by district.

**Key metrics:**

| What you see | Term | What it means |
|---|---|---|
| Live schools count | Live school | Schools that sent a measurement in the last 21 days |
| Drop-off count | Drop-off | Schools silent for 28+ days — without intervention unlikely to return |
| Drop-off rate | Drop-off rate | Drop-offs ÷ total installed schools, as a percentage. Rising rate = support effort needed |

{% hint style="warning" %}
A drop-off rate above 10% is a signal to increase follow-up with school IT focal points or to plan re-installation visits.
{% endhint %}

---

## Related pages

- [Metric Glossary](metric-glossary.md) — full A–Z definitions
- [Using the Data](access-channels.md) — dashboard vs. API access
- [Uptime Explained](../getting-started/uptime-explained.md) — how the availability metric is calculated
