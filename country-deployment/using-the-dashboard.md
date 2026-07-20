# Using the Dashboard

Giga Meter data is published through an [Apache Superset](https://superset.giga.global) dashboard. Tabs show school summaries, speed and latency trends, district breakdowns, per-measurement tables, app-version tracking, and installation health. This page is a screen-by-screen reference.

For how to get an account and which access channel suits which user, see the [Data Analysis Lead Guide](../docs/deployment/data-analysis-lead.md).

{% hint style="info" %}
**Getting access:** create an account at [superset.giga.global](https://superset.giga.global), then share your registered email with the Giga team, who assign a country-level role. Without a role, you can log in but will not see any data.
{% endhint %}

***

### Superset Dashboards' sections

All tabs are reached from the tab bar at the top of the dashboard.

| Screen                             | What it answers                                                                                             |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Summary**                        | How many schools are on the map, how many report through Giga Meter, and headline speed and latency figures |
| **Connectivity · Speed & Latency** | Daily speed and latency trends, and how speeds are distributed across schools                               |
| **Connectivity · District**        | Average speed broken out by district, plus a per-school table with sparklines                               |
| **Data Tables · Registered**       | One row per registered school, key operational fields for follow-up                                         |
| **Data Tables · Measurements**     | One row per individual test, including Wi-Fi diagnostics captured at measurement time                       |
| **App Tracking**                   | Which Giga Meter version is running across the country; daily reporting counts                              |
| **Installation Tracking**          | Who is live, who has gone quiet, and drop-off rate by district                                              |

<details>

<summary>Screen 1 - Summary</summary>

The opening view. Two headline numbers, schools on the map and schools reporting through Giga Meter, followed by headline speed and latency figures.



<figure><img src="../.gitbook/assets/Superset 1.png" alt=""><figcaption></figcaption></figure>

| What you see                       | Term           | What it means                                                              |
| ---------------------------------- | -------------- | -------------------------------------------------------------------------- |
| Schools on Giga Maps (e.g. 1.19k)  | Giga Maps      | Schools that have been located and published on Giga Maps                  |
| Schools with Giga Meter (e.g. 81)  | Giga Meter     | Of the mapped schools, how many run the app and stream measurements        |
| Live (e.g. 75)                     | Live school    | Schools that sent a reading within the last 21 days                        |
| Drop-off (e.g. 5)                  | Drop-off       | Schools silent for 29+ days, unlikely to come back without a site visit    |
| At-risk (e.g. 1)                   | At-risk school | Schools in the 22-28-day quiet window                                      |
| Average download (e.g. 85.59 Mbps) | Download speed | Average across all schools and all measurements in scope                   |
| Average latency (e.g. 59 ms)       | Latency        | About the upper edge of what feels instant in a video call                 |
| Total measurements (e.g. 32.4k)    | Measurement    | Individual Giga Meter tests across all schools in the selected time window |

</details>

<details>

<summary>Screen 2 - Connectivity · Speed &#x26; Latency</summary>

Daily speed and latency trends, plus box-plot distributions showing how consistent the experience is across schools.



<figure><img src="../.gitbook/assets/Superset 2.png" alt=""><figcaption></figcaption></figure>

| What you see | Term               | What it means                                                              |
| ------------ | ------------------ | -------------------------------------------------------------------------- |
| Black line   | Download speed     | Average daily download, in Mbps                                            |
| Blue line    | Upload speed       | Average daily upload, usually below download                               |
| Box plot     | Speed distribution | Shaded box = middle 50% of schools; dots = outliers                        |
| Lower chart  | Latency            | Average daily latency in milliseconds                                      |
| Y-axis unit  | Milliseconds (ms)  | Under 50 ms comfortable for video calls; over 200 ms causes noticeable lag |

</details>

<details>

<summary>Screen 3 - Connectivity · District</summary>

Average speed broken out by administrative district, then a per-school table with sparklines.

<figure><img src="../.gitbook/assets/Superset 2.1.png" alt=""><figcaption></figcaption></figure>



| What you see        | Term             | What it means                                                                   |
| ------------------- | ---------------- | ------------------------------------------------------------------------------- |
| Grey bars           | Download speed   | Average download per district                                                   |
| Green bars          | Upload speed     | Side-by-side with download, makes asymmetric links easy to spot                 |
| "Last value" column | Load speed       | The most recent single Giga Meter test reading                                  |
| "Weekly Avg" column | Rolling average  | Average of every measurement from the last seven days                           |
| "WoW %" column      | Week-over-Week % | -91% means this week's average is 91% lower than last week, worth investigating |

</details>

<details>

<summary>Screen 4 - Data Tables · Registered</summary>

One row per school that has registered through Giga Meter. Most useful for operational follow-up.

<figure><img src="../.gitbook/assets/Superset 3 (1).png" alt=""><figcaption></figcaption></figure>

| Column name                 | What it means                                                               |
| --------------------------- | --------------------------------------------------------------------------- |
| `school_id_govt`            | The country's official school identifier, different from Giga's internal ID |
| `num_measurements`          | Total Giga Meter tests the school has ever run                              |
| Days since last measurement | 0 = sent a reading today; non-zero is an early warning                      |
| `num_devices_registered`    | How many computers at the school are linked to Giga Meter                   |
| `most_recent_app_version`   | Newest Giga Meter build any device at the school is running                 |

{% hint style="success" %}
Sort by "days since last measurement" descending to surface schools that need follow-up first.
{% endhint %}

</details>

<details>

<summary>Screen 5 - Data Tables · Measurements</summary>

One row per individual Giga Meter test, including Wi-Fi diagnostics captured at measurement time.



<figure><img src="../.gitbook/assets/Superset 3.1 (1).png" alt=""><figcaption></figcaption></figure>



| Column name          | What it means                                                              |
| -------------------- | -------------------------------------------------------------------------- |
| `load_speed`         | Download speed recorded by this specific test, in Mbps                     |
| `isp_asn_clean`      | Identifies which provider's network served this test                       |
| `avg_latency`        | Latency recorded by this specific test, in ms                              |
| `isp_clean`          | ISP name, cleaned from what the app captured                               |
| `detected_wifi_ssid` | Name of the Wi-Fi network the device was on during the test                |
| Wi-Fi signal         | Signal strength in dBm, closer to zero is stronger (-60 healthy; -85 weak) |
| Wi-Fi TX rate        | Data rate to the router in Mbps, drops as the wireless link weakens        |

{% hint style="info" %}
If a school shows low `load_speed` but healthy latency and strong Wi-Fi signal, the bottleneck is likely on the ISP side, not the school's internal network.
{% endhint %}

</details>

<details>

<summary>Screen 6 - App Tracking</summary>

Which version of Giga Meter is deployed across the country and how many schools send data each day.



<figure><img src="../.gitbook/assets/Superset 4.png" alt=""><figcaption></figcaption></figure>

| What you see | What it means                                                               |
| ------------ | --------------------------------------------------------------------------- |
| Donut chart  | Each wedge = a different Giga Meter build. A single wedge = uniform version |
| Bar chart    | Each bar = number of schools that sent at least one measurement that day    |
| Grey line    | 7-day rolling count, smooths weekend dips and reveals the growth trend      |

{% hint style="success" %}
After a version update, watch this screen for schools still on older builds. A fragmented donut means some devices missed the update.
{% endhint %}

</details>

<details>

<summary>Screen 7 - Installation Tracking</summary>

Health-check view. Shows who is live, who has gone quiet, and drop-off rate by district.



<figure><img src="../.gitbook/assets/Superset 5.png" alt=""><figcaption></figcaption></figure>

| What you see       | What it means                                                            |
| ------------------ | ------------------------------------------------------------------------ |
| Live schools count | Schools that sent a measurement in the last 21 days                      |
| Drop-off count     | Schools silent for 29+ days, without intervention unlikely to return     |
| Drop-off rate      | Drop-offs ÷ total installed schools. Rising rate = support effort needed |

{% hint style="warning" %}
A drop-off rate above 10% is a signal to increase follow-up with school IT focal points or to plan re-installation visits.
{% endhint %}

</details>

***

### Related pages

* [Data Analysis Lead Guide](../docs/deployment/data-analysis-lead.md)
* [Metric Glossary](../installation/metric-glossary.md)
* [Installation Lead Guide](../docs/deployment/installation-lead.md)
