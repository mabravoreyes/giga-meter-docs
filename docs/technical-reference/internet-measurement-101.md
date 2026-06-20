# Internet Measurement 101

A guide for interpreting Giga Meter data in context — why different measurement tools produce different numbers, and what each type actually tells you.

---

## The question this page answers

Why might Giga Meter show 5 Mbps at a school when the ISP contract says 100 Mbps?

They are measuring different things, at different points in the network, using different methods. Neither reading is wrong — they are answers to different questions.

---

## The network path

Every data transfer between a school and the internet travels through a chain of links. Each link can limit performance independently of the others.

```
School device
    ↓
Wi-Fi (radio link to access point)
    ↓
LAN switch (wired internal network)
    ↓
Router / CPE (school's internet gateway)
    ↓
ISP backhaul (the ISP's delivery link to the school)
    ↓
ISP core network
    ↓
Internet backbone
    ↓
Remote server (M-Lab test server, content platforms, etc.)
```

A measurement captures performance **from the point where it's taken to the point it's taken against**. This is why where you measure matters as much as what you measure.

---

## Three measurement perspectives

### 1. ISP-reported speed

**What it measures:** The speed at the ISP's handoff point — typically the CPE (customer premises equipment) or the port where the ISP's network meets the school's internal network.

**What it does not capture:**
- Wi-Fi performance inside the school
- Congestion on the school's internal LAN
- Router limitations
- The number of devices sharing the connection at that moment

**Typical source:** ISP monitoring dashboards, NOC reports, contract SLAs.

**What to use it for:** Verifying that the ISP is delivering what they contracted to deliver — to the school's door, not to the school's devices.

---

### 2. At-router / network infrastructure measurement

**What it measures:** Speed at the school's gateway or router — the point where the ISP's link meets the school's internal network. Tools like LibreNMS measure traffic on network interfaces and can show throughput per link segment.

**What it does not capture:**
- Wi-Fi interference or congestion
- Per-device performance
- The experience of a student at a classroom device

**Typical source:** Network monitoring tools deployed on routers and access points (e.g., LibreNMS, SNMP polling).

**What to use it for:** Diagnosing whether a problem is at the ISP level or inside the school. If router throughput = ISP contracted speed but device speeds are low, the problem is internal (Wi-Fi, LAN congestion, too many concurrent users).

---

### 3. End-to-end (E2E) device measurement

**What it measures:** The full path from a connected device to a remote test server — capturing every link in the chain, including Wi-Fi, LAN, router, ISP backhaul, and the internet path to the server.

**This is what Giga Meter measures.** NDT7 runs from the school device and measures what that device actually received — which is what students and teachers experience.

**What it captures that other methods don't:**
- Wi-Fi signal quality at the point of use
- Congestion from concurrent users on the same access point or channel
- Router and LAN bottlenecks
- Real-world variability (peak vs. off-peak, device load)

**What to use it for:** Understanding the actual learning environment — whether the connectivity a school officially "has" is the connectivity that students and teachers can actually use.

---

## Why E2E speeds are typically lower than contracted speeds

Even when an ISP delivers exactly what they contracted, E2E device measurements will often be lower. This is normal and expected. Common reasons:

| Source of gap | What causes it |
|---|---|
| Wi-Fi overhead | Wi-Fi protocols add overhead; 2.4 GHz bands are especially congested in dense environments |
| Concurrent users | All devices on the same access point share bandwidth; 30 students streaming = very different per-device speed than 1 student testing alone |
| Access point placement | A device far from the AP or separated by walls will receive lower signal and lower speeds |
| Router processing limits | Consumer-grade routers can become a bottleneck at high speeds |
| TCP protocol behaviour | NDT7 uses TCP, which adds protocol overhead and takes time to ramp up to maximum throughput |
| Path congestion | Routing through the public internet adds variability depending on time of day and server load |
| Test server distance | A test server farther away will show higher latency; latency affects TCP throughput |

---

## What triangulation tells you

The most diagnostic picture comes from comparing all three measurement types together. This is the approach Mongolia uses — combining LibreNMS (at-router) with Giga Meter (E2E device) to isolate where problems sit.

| Pattern | What it means |
|---|---|
| ISP speed ≈ contracted, device speed low | Problem is inside the school — Wi-Fi, LAN congestion, too many users, access point placement |
| ISP speed low, device speed low | Problem is the ISP — under-delivering against the contract |
| ISP speed ≈ contracted, at-router speed low | Problem is at the router or CPE — hardware bottleneck or configuration issue |
| Device speed low at peak, high off-peak | Congestion from concurrent users — the link is adequate but shared capacity is insufficient |
| High variability in device speed | Unstable ISP delivery or Wi-Fi interference — consistent low speed is a different problem than high variance |

---

## What Giga Meter does and does not measure

### Giga Meter measures:
- **Download throughput** — how fast data reaches the device from M-Lab (NDT7)
- **Upload throughput** — how fast data leaves the device to M-Lab (NDT7)
- **Latency** — round-trip time to the M-Lab server (reported by NDT7)
- **Uptime** — whether the device has internet connectivity every 15 minutes during school hours (Cloudflare ping)

### Giga Meter does not measure:
- **Jitter** (latency variation) — not reported in the current version
- **Packet loss** — not reported in the current version
- **Wi-Fi signal strength at the device** — measured and captured in metadata but not surfaced in the main metrics
- **LAN segment performance** — Giga Meter is an E2E tool; it cannot isolate specific LAN links
- **Number of concurrent users** — Giga Meter does not know how many other devices are active during the test; speeds measured during high-use periods will be lower

---

## Interpreting results in context

**A single measurement is rarely conclusive.** Connectivity is variable — by time of day, number of users, ISP congestion, and many other factors. Giga Meter runs up to four tests per day across different time slots specifically to capture this variability.

When reviewing school data:
- Look at **medians and distributions**, not individual tests
- Compare **peak hours vs. off-peak** — large differences suggest congestion rather than ISP underperformance
- Flag schools with **high variability** separately from schools with **consistently low speeds** — they need different interventions
- Use speed data alongside **uptime data** — a school with good average speeds but frequent outages has a different problem than one with consistently low speeds

→ [Metric Glossary](metric-glossary.md) — definitions for every metric\
→ [Measurement Protocols](measurement-protocols.md) — how NDT7 and ping tests work\
→ [API Reference](api-reference.md) — accessing raw measurement data
