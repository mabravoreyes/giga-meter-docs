# Network Destinations & Firewall Configuration

This page is for IT administrators who need to configure firewalls, proxy servers, or content filtering systems to allow Giga Meter traffic.

{% hint style="info" %}
All Giga Meter connections use **DNS-resolvable hostnames** over **HTTPS (port 443)**. The app does not connect to hardcoded static IP addresses. A DNS-based domain whitelist is sufficient; no static IP list is required or maintained.
{% endhint %}

***

### Complete destination list

| Service                   | Hostname                                       | Purpose                                                                    | Protocol           | Port |
| ------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------- | ------------------ | ---- |
| Giga Meter Backend API    | `uni-ooi-giga-meter-backend.azurewebsites.net` | Device registration, measurement upload, configuration sync, feature flags | HTTPS (REST)       | 443  |
| M-Lab Locate Service      | `locate.measurementlab.net`                    | Server discovery, selects the nearest NDT speed test server                | HTTPS (REST)       | 443  |
| M-Lab NDT Servers         | `*.measurementlab.net`                         | Speed test execution (download/upload throughput measurement)              | WebSocket over TLS | 443  |
| IPinfo API                | `api.ipinfo.io`                                | IP geolocation, ISP/ASN identification                                     | HTTPS (REST)       | 443  |
| GeoJS                     | `ipv4.geojs.io`                                | IP address detection (fallback)                                            | HTTPS (REST)       | 443  |
| Cloudflare                | `speed.cloudflare.com`                         | Ping and latency measurements                                              | HTTPS              | 443  |
| Sentry (error monitoring) | `excubo.unicef.io`                             | Application crash reporting, self-hosted by UNICEF ICTD                    | HTTPS              | 443  |
| Auto-update server        | `github.com` / `*.github.com`                  | Application auto-update checks and download                                | HTTPS              | 443  |

***

### Minimum firewall whitelist

Add these outbound rules. All traffic is port 443 HTTPS only; no inbound connections are required.

| Rule | Domain                                         | Notes                                                       |
| ---- | ---------------------------------------------- | ----------------------------------------------------------- |
| 1    | `uni-ooi-giga-meter-backend.azurewebsites.net` | Core API, required                                          |
| 2    | `locate.measurementlab.net`                    | M-Lab server discovery, required                            |
| 3    | `*.measurementlab.net`                         | M-Lab speed test servers (dynamic pool), required           |
| 4    | `api.ipinfo.io`                                | IP geolocation, required                                    |
| 5    | `ipv4.geojs.io`                                | IP detection fallback, required                             |
| 6    | `speed.cloudflare.com`                         | Ping measurements, required                                 |
| 7    | `excubo.unicef.io`                             | Error monitoring, optional, not needed for core measurement |
| 8    | `github.com` / `*.github.com`                  | App updates, optional, can be managed manually              |

***

### Traffic characterization

#### Speed test (NDT7 protocol)

| Attribute    | Detail                                                                                         |
| ------------ | ---------------------------------------------------------------------------------------------- |
| Protocol     | NDT7 over WebSocket/TLS (wss://)                                                               |
| Port         | 443                                                                                            |
| Direction    | Bidirectional, download: server→client; upload: client→server                                  |
| Data content | Random binary data (bulk transfer for throughput measurement)                                  |
| Duration     | \~10-15 seconds per test                                                                       |
| Frequency    | Up to 4 tests per day: 1 at device startup + 3 in random windows (8-12h, 12-16h, 16-20h local) |
| Destination  | Dynamically selected nearest M-Lab server                                                      |

{% hint style="warning" %}
Speed test traffic produces short, high-bandwidth bursts that may resemble suspicious activity in traffic monitoring systems. This is expected: the test needs to saturate the connection to measure its capacity. Each burst lasts approximately 10-15 seconds and occurs up to 4 times per day.
{% endhint %}

#### Ping / latency measurement

| Attribute    | Detail                                            |
| ------------ | ------------------------------------------------- |
| Protocol     | HTTPS                                             |
| Port         | 443                                               |
| Target       | `speed.cloudflare.com`                            |
| Data content | Minimal HTTP request/response for round-trip time |
| Frequency    | Every 15 minutes, 8am-8pm local time              |
| Data size    | Negligible (< 1 KB per request)                   |

#### Measurement data upload

| Attribute      | Detail                                                               |
| -------------- | -------------------------------------------------------------------- |
| Protocol       | HTTPS REST API (POST)                                                |
| Port           | 443                                                                  |
| Destination    | `uni-ooi-giga-meter-backend.azurewebsites.net`                       |
| Authentication | Bearer token in HTTP Authorization header                            |
| Frequency      | After each speed test (up to 4x/day) + batched sync for offline data |
| Data size      | \~2-5 KB per measurement                                             |

#### Configuration sync

| Attribute   | Detail                                         |
| ----------- | ---------------------------------------------- |
| Protocol    | HTTPS REST API (GET)                           |
| Port        | 443                                            |
| Destination | `uni-ooi-giga-meter-backend.azurewebsites.net` |
| Frequency   | Every 6 hours                                  |
| Data size   | \~1-2 KB                                       |

#### IP geolocation lookup

| Attribute   | Detail                              |
| ----------- | ----------------------------------- |
| Protocol    | HTTPS REST API (GET)                |
| Port        | 443                                 |
| Destination | `api.ipinfo.io`                     |
| Frequency   | Once per unique IP address (cached) |
| Data size   | \~500 bytes response                |

#### Error reporting

| Attribute   | Detail                            |
| ----------- | --------------------------------- |
| Protocol    | HTTPS                             |
| Port        | 443                               |
| Destination | `excubo.unicef.io`                |
| Frequency   | Only when errors or crashes occur |
| Data size   | \~5-20 KB per error event         |

***

### Traffic summary

| Traffic type      | Pattern                  | Bandwidth impact                           |
| ----------------- | ------------------------ | ------------------------------------------ |
| Speed test (NDT7) | 4 bursts/day, \~15s each | High, intentional, measures max throughput |
| Ping              | Every 15 min, 8am-8pm    | Negligible                                 |
| Data upload       | Up to 4x/day             | Very low (\~5 KB per upload)               |
| IP lookup         | Rare, only on IP change  | Negligible                                 |
| Config sync       | Every 6 hours            | Negligible                                 |
| Error reporting   | Sporadic                 | Very low                                   |

***

### M-Lab server selection

M-Lab's speed test infrastructure is a globally distributed network of servers. Giga Meter does not connect to a fixed server; it selects the nearest one at the time of each test:

1. **Discovery:** The app calls `locate.measurementlab.net` over HTTPS to request the nearest available server
2. **Selection:** The Locate Service returns the nearest NDT server as a DNS hostname (not an IP address)
3. **Test:** The app connects to the selected server via WebSocket/TLS (wss://) on port 443

Because M-Lab's server pool is dynamic, with servers regularly added, removed, and maintained, a static IP list is not feasible. The DNS wildcard `*.measurementlab.net` covers both the Locate Service and all NDT servers globally and is the correct whitelisting approach.

***

### Application architecture summary

| Layer            | Technology                          |
| ---------------- | ----------------------------------- |
| Frontend         | Angular 19 + Ionic 6                |
| Desktop runtime  | Electron 29                         |
| Backend          | NestJS (Node.js / TypeScript)       |
| Database         | PostgreSQL                          |
| Speed test       | NDT7 (M-Lab), Apache 2.0            |
| Cloud hosting    | Microsoft Azure                     |
| Error monitoring | Sentry (self-hosted by UNICEF ICTD) |

**Data flow:**

1. School installs app → registers with school ID → backend saves registration
2. App runs scheduled speed tests (NDT7) and ping measurements (Cloudflare)
3. Results uploaded to Giga Backend via HTTPS REST API
4. Aggregated data displayed on [Giga Maps](https://maps.giga.global/) (public)
5. Offline resilience: if the network is unavailable, measurements are stored locally and synced when connectivity returns (up to 7 days of offline storage)

***

### Related pages

* [Privacy & Security](../docs/security/privacy-and-security.md)
* [FAQ - What data does Giga Meter transmit?](../docs/troubleshooting/faq.md)
* [Measurement Protocols](../docs/technical-reference/measurement-protocols.md)
