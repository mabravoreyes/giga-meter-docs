# FAQ

***

### How can I view my school's data?

You can view results in two ways:

1. **In the app** — the last 10 successful measurements are visible in the app's Data page.
2. **On Giga Maps** — visit [maps.giga.global/map](https://maps.giga.global/map), type your school name or ID in the left-hand panel, and select it to view results over time.

The dot next to each school is colour-coded by connectivity level:

**Green** — Good connectivity. The school meets or exceeds the selected benchmark.

<figure><img src="../../.gitbook/assets/maps-green-good.png" alt="Celetyuma Primary School — 51.99 Mbps, green dot"><figcaption></figcaption></figure>

**Yellow** — Moderate connectivity. The school is below the benchmark but has a working connection.

<figure><img src="../../.gitbook/assets/maps-yellow-moderate.png" alt="Lonwabo Senior Secondary School — 7.87 Mbps, yellow dot"><figcaption></figcaption></figure>

**Red** — Slow connectivity. The school is significantly below the benchmark.

<figure><img src="../../.gitbook/assets/maps-red-slow.png" alt="Embekweni Junior Primary School — 0.8 Mbps, red dot"><figcaption></figcaption></figure>

A **blue** dot means no recent data has been received — the device may be off or the app may need reinstalling.

Copy the URL on your browser after selecting your school — you can bookmark it for direct access any time.

***

### What data does Giga Meter transmit to Giga?

The app transmits only network performance data. No browsing history, search activity, or personal files are ever collected.

<table><thead><tr><th width="169.924560546875">Field</th><th width="138.1883544921875">Example</th><th>What it is</th></tr></thead><tbody><tr><td><strong>Download speed</strong></td><td>10 Mbps</td><td>Rate at which data travels from an M-Lab server to the device (NDT7 protocol, 10-second test)</td></tr><tr><td><strong>Upload speed</strong></td><td>5.7 Mbps</td><td>Rate at which data travels from the device to an M-Lab server (NDT7 protocol, 10-second test)</td></tr><tr><td><strong>Latency</strong></td><td>3 ms</td><td>Round-trip time for a small packet to travel from the device to a server and back</td></tr><tr><td><strong>Packet loss</strong></td><td>0.5%</td><td>Percentage of data packets sent that never arrive at their destination</td></tr><tr><td><strong>Uptime</strong></td><td>99%</td><td>Proportion of school hours (8 AM–8 PM) during which the connection is confirmed reachable, derived from automated pings</td></tr><tr><td><strong>ISP / ASN</strong></td><td>AS8193 Uzbektelekom</td><td>The internet service provider and their Autonomous System Number — a unique identifier assigned by global internet authorities</td></tr><tr><td><strong>IP address</strong></td><td>84.54.71.31</td><td>The public IP address assigned to the school's connection at the time of measurement</td></tr><tr><td><strong>Test server location</strong></td><td>Chennai, IN</td><td>Geographic location of the M-Lab measurement server used in the speed test</td></tr><tr><td><strong>Device type</strong></td><td>windows</td><td>Operating system running the measurement application</td></tr><tr><td><strong>Network name (SSID)</strong></td><td>MERCUSYS_43A4</td><td>Name of the Wi-Fi network the device is connected to at the time of the test</td></tr><tr><td><strong>Wi-Fi standard</strong></td><td>802.11n</td><td>Wi-Fi protocol version in use (802.11n = Wi-Fi 4, 802.11ac = Wi-Fi 5, 802.11ax = Wi-Fi 6)</td></tr><tr><td><strong>Wi-Fi channel</strong></td><td>10</td><td>Radio frequency channel the router is broadcasting on</td></tr><tr><td><strong>Wi-Fi signal level</strong></td><td>−70.5 dBm</td><td>Signal strength received by the device. Closer to 0 = stronger; below −80 dBm is poor</td></tr><tr><td><strong>Wi-Fi transmit rate</strong></td><td>300 Mbps</td><td>Speed at which the device's wireless adapter sends data to the router — the wireless link rate, not the internet speed</td></tr><tr><td><strong>Wi-Fi adapter model</strong></td><td>Intel Wireless-AC 9560</td><td>Hardware model of the Wi-Fi adapter inside the measurement device</td></tr></tbody></table>

***

### Will Giga have access to any other information on my computer?

No. The application does not have access to any data stored on your computer other than the data described above.

***

### Who will have access to my school connectivity data?

Upload speed, download speed, latency, and ping test results will be shared with the public in combination with information about the registered school. This data is displayed on Giga Maps. No personal data is shared.

***

### What is a School ID?

A School ID is a unique identifier for your school, provided by the government. Formats vary by country but it typically looks like `BR12345` or `12345678`.

***

### How do I find my School ID?

Ask your school administrator or IT department. The school ID is the number used in your national school registration system.

***

### Can I close the application?

Yes. Clicking the close button will close the window, but the app will continue running in the background and will keep reporting your connectivity status.

***

### How do I update the application?

When a new version is available, a notification pop-up will appear — click **Restart** to update. You can also visit [meter.giga.global](https://meter.giga.global/) at any time to download and install the latest version.

***

### When do speed tests run?

Up to four speed tests run per day:

* First test: within 15 minutes of the device being powered on
* Remaining tests: within the time slots 8 AM–12 PM, 12 PM–4 PM, and 4 PM–8 PM (local time)

Ping tests run every 15 minutes between 8 AM and 8 PM local time.

You can also trigger a manual test at any time.

***

### Where can I see past measurement results?

* **In-app:** Last 10 successful tests are shown in the measurement dashboard under the Data page.
* **Giga Maps:** Daily averages are published to [maps.giga.global](https://maps.giga.global/). Find your school to see how its connectivity compares globally.

***

### Can I change my school ID?

If you registered with the wrong school ID, you can unregister and re-register. See [Troubleshooting — Registered with the wrong school ID](troubleshooting.md#registered-with-the-wrong-school-id).

***

### Can I install Giga Meter on more than one computer?

Yes — and we encourage it. If multiple machines report data from the same school, measurements are more reliable.

***

### What kind of data does Giga Meter access?

Only system and network information needed to measure internet quality: connection speed, availability, network details, and device type. It does not access personal files, browsing history, or content.

***

### How does Giga Meter help improve internet access?

Giga Meter doesn't fix internet connections directly, but it makes problems visible. This data helps governments and providers identify and prioritize improvements where they're needed most.

***

For further guidance, visit [meter.giga.global](https://meter.giga.global/) or the help section directly in the app.
