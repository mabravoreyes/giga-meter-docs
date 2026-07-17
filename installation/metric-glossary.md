# Metric Glossary

Plain-language definitions for the terms and metrics used in Giga Meter, Giga Maps, and the school connectivity dashboards.

***

### A

**API (Application Programming Interface)** An interface that lets different computer systems exchange information automatically. Giga Maps exposes its data through a public API so partners can build on top of it.

**App version** The release number of the Giga Meter app installed at a school (for example 2.0.2). Newer versions fix bugs and add measurement features.

**ASN (Autonomous System Number)** A unique number that identifies an internet provider's network on the global internet, such as AS8926. Used to confirm which carrier is serving the school.

**At-risk school** A school whose last measurement was sent between 22 and 28 days ago. It has not gone silent yet, but may drop off without follow-up.

**Availability** See _Uptime_.

***

### B

**Bandwidth** The maximum amount of data that can pass through an internet connection per second, usually reported in megabits per second (Mbps). Higher bandwidth means more devices can stream, call, and load pages at the same time.

***

### C

**Connected / Not connected / Unknown** The three connectivity labels Giga assigns to every mapped school. "Connected" means the school has confirmed internet service; "Not connected" means it does not; "Unknown" means there is not yet enough information to tell.

**Connectivity status** The summary judgement of whether a school has working internet, drawn from multiple sources including school surveys, partner reports, and Giga Meter measurements.

***

### D

**Dashboard** A single screen that brings together charts, tables, and key numbers so a user can monitor a topic at a glance. Giga's school-connectivity dashboards are built in Apache Superset.

**Data point** A single recorded value, such as one school's download speed at one moment in time. A chart is built from many data points.

**Days since last measurement** How long it has been, in days, since the school's Giga Meter app last sent a reading. A growing number is an early warning that the school is going offline or that the device has been switched off.

**Distribution (statistical)** A chart that shows how a set of values is spread across a range, rather than just their average. Useful for seeing whether most schools cluster around a typical speed or whether a few outliers pull the average up.

**Download speed** The rate at which a school receives data from the internet, for example when loading a webpage or streaming a video. Measured in megabits per second (Mbps).

**Drop-off** A school that has not sent any measurement in 29 or more days. After this point Giga considers the device unlikely to return without additional support, such as a site visit.

**Drop-off rate** The share of installed schools that have dropped off, expressed as a percentage. A rising drop-off rate means support effort needs to increase.

***

### F

**Fair-Use Policy (FUP)** Rules that slow down or temporarily suspend a connection after a school exceeds its monthly data allowance. The exact rules vary by supplier and should be written into the contract.

***

### G

**Giga Maps** Giga's public, interactive map showing every school that has been located, along with its known connectivity status. Open to governments, partners, and the public. [maps.giga.global](https://maps.giga.global/)

**Giga Meter** A free Giga app that runs connectivity tests from a school's computer. The results (speed, latency, Wi-Fi quality) flow into the Giga dashboards daily. [meter.giga.global](https://meter.giga.global/)

***

### I

**ISP (Internet Service Provider)** The company that supplies internet to the school. Different ISPs may deliver very different real-world speeds even on the same contract.

***

### L

**Latency** The delay between a school's device asking for something and the first response coming back. Measured in milliseconds (ms). Low latency matters most for video calls, online classes, and other real-time services.

**Live school** A school whose last measurement was sent within the last 21 days. The device is actively reporting and the link can be assumed healthy.

**Load speed** The download speed measured during a single Giga Meter test, in megabits per second. A school has many load-speed values over time, one per test run.

***

### M

**Mbps (megabits per second)** The standard unit for internet speed. One megabit is one million bits. As a rough guide, smooth video calls need around 1-2 Mbps per participant; a class watching HD video needs 5 Mbps or more.

**Measurement** A single connectivity test run by the Giga Meter app at a school. Each measurement records download speed, upload speed, latency, and details about the Wi-Fi network at that moment.

**Milliseconds (ms)** Thousandths of a second, the unit used for latency. Anything under 50 ms feels instant for most uses; over 200 ms makes video calls feel awkward.

***

### N

**Network Operations Centre (NOC)** A facility where technicians watch the network around the clock, spot incidents, and coordinate repairs. Required by Giga's connectivity recommendations for any serious school programme.

**Number of devices registered** How many distinct computers have been linked to a school's Giga Meter account. More devices generally mean more frequent measurements and less risk that one broken device takes the school offline.

***

### R

**Real-time (RT) data** Measurements that are available soon after they are taken, rather than aggregated once a month. In the Giga context, real-time data is published daily.

**Rolling average (e.g., 7-day)** An average recomputed every day from only the most recent N days. Smooths out daily ups and downs so an underlying trend is easier to see.

***

### S

**School ID (government)** The school's official identifier in the national education ministry's records. Different from the Giga ID; both are kept so Giga data can be reconciled with government data.

**Service Level Agreement (SLA)** A contract term defining the service quality the supplier promises. Typical figures include 99% uptime in cities, minimum speeds, and maximum repair times. The dashboard's availability charts are how an SLA is checked in practice.

**Speed distribution** A chart that shows how speeds vary across all schools, not just on average. The wider the box, the more uneven the experience between schools.

**SSID (Service Set Identifier)** The public name of a Wi-Fi network, what shows up when a device scans for nearby networks.

**Superset** Apache Superset, the open-source dashboard tool Giga uses to publish school connectivity data. Access it at [superset.giga.global](https://superset.giga.global). The top bar (Dashboards, Charts, Datasets, SQL) comes from Superset's standard interface.

***

### T

**Time series** A chart or table that shows how a single value changes over time. The wavy line next to each school's name in the dashboard is a time series of its daily speed.

***

### U

**Upload speed** The rate at which a school sends data to the internet, for example the outgoing side of a video call or uploading homework. Usually lower than download speed.

**Uptime (availability)** The percentage of time the internet connection is working and usable. Giga Meter measures uptime during school hours (8am-8pm) on days when the device is powered on. Because it is measured only during school hours, a 99% target means the connection can be unreachable for at most about 3.6 hours of school time in a month.

***

### W

**Week-over-Week (WoW) %** The percentage change compared with the previous week. A WoW of -38% means this week's value is 38% lower than last week's; "null" means there is not enough history yet to compute it.

**Wi-Fi 6 (IEEE 802.11ax)** A modern Wi-Fi standard that offers faster speeds and handles many simultaneous users better than older Wi-Fi. Required for Giga's recommended classroom access points.

**Wi-Fi frequency** The radio band a Wi-Fi network uses, reported in megahertz. Around 2400 means the 2.4 GHz band (longer range, more interference); around 5000 means the 5 GHz band (faster, shorter range).

**Wi-Fi quality** A composite score the computer reports for how clean the wireless link is, combining signal strength and interference. Higher is better.

**Wi-Fi signal** How strong the Wi-Fi radio signal is at the measuring device, in dBm. The closer to zero, the stronger, so -60 is a healthy signal and -85 is weak.

**Wi-Fi TX rate** The data rate at which the device is currently sending to the Wi-Fi router, in megabits per second. Drops when the signal weakens, even if the contracted internet speed is unchanged.

**Wireless LAN (WLAN)** The local wireless network inside a school, what most people simply call "the Wi-Fi". Sits between the school's devices and the Customer Premises Equipment (CPE) that connects to the outside internet.

***

### Related pages

* [Measurement Protocols](../docs/technical-reference/measurement-protocols.md) - how Giga Meter runs its tests
* [Data Analysis Lead Guide](../docs/deployment/data-analysis-lead.md) - where each term appears on screen
* [Data Governance & Privacy](../docs/technical-reference/data-governance.md) - what data is shared and with whom
