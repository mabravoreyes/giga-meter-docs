# Troubleshooting

Find your issue below, grouped by where in the process it appears. For general questions about how the app works, see the [FAQ](faq.md).

---

## Quick reference

| Symptom | Section |
|---|---|
| Windows SmartScreen blocks the installer | [Installation — SmartScreen warning](#installation--updates) |
| App says you have an old version | [Installation — Old version](#installation--updates) |
| School not found when entering the ID | [Registration — School not found](#registration) |
| Registered with the wrong school | [Registration — Wrong school ID](#registration) |
| Wrong country detected | [Registration — Country not detected correctly](#registration) |
| Tests failing or no data on Giga Maps | [After installation — Tests not running](#after-installation) |
| School shows as "Unknown" on Giga Maps | [After installation — School appears Unknown](#after-installation) |

---

{% tabs %}
{% tab title="Installation & updates" %}

### SmartScreen warning

{% hint style="warning" %}
**What you'll see:** "Windows protected your PC — Microsoft Defender SmartScreen prevented an unrecognised app from starting."
{% endhint %}

This is a standard Windows warning for apps not yet in Microsoft's database. The app is published by UNICEF and safe to install.

1. Click **More info**
2. Click **Run anyway**

---

### User Account Control (UAC) prompt

{% hint style="warning" %}
**What you'll see:** A dialog asking "Do you want to allow this app to make changes to your device?" Publisher: UNICEF.
{% endhint %}

Click **Yes**. This opens the Setup Wizard. If you do not have admin rights on the device, contact your IT department.

---

### Old version / no update prompt

{% hint style="warning" %}
**What you'll see:** The app warns that you are running an outdated version, or you dismissed the update notification.
{% endhint %}

1. Visit [meter.giga.global](https://meter.giga.global/)
2. Download and install the latest version

The new installation overwrites the older version automatically. Your school registration is preserved — you do not need to register again.

{% endtab %}

{% tab title="Registration" %}

### School not found

{% hint style="warning" %}
**What you'll see:** No results appear after entering the school ID and clicking Search.
{% endhint %}

1. Check for extra spaces before or after the ID — remove them and search again.
2. If the ID starts with a zero (`0`), try omitting the leading zero and searching again.
3. Try searching by school name instead of ID.
4. If the school still cannot be found, contact your focal point at the Ministry or UNICEF Country Office — the school may not yet be registered in Giga's systems.

---

### Registered with the wrong school ID

{% hint style="warning" %}
**What you'll see:** Giga Meter is running but showing data for the wrong school.
{% endhint %}

1. Open Giga Meter and go to **Settings**
2. Click **Logout**, then enter your school ID and click **Logout** again to confirm
3. You will return to the registration screen — follow [Step 11 of the Installation Guide](../installation/installation-guide.md#step-11--accept-the-policies) to re-register with the correct ID

{% hint style="warning" %}
Logging out removes the registration for **all users on this device**. No measurements will be recorded for the previously registered school until re-registration is complete.
{% endhint %}

After re-registering, switch to any other Windows user accounts on the device and open Giga Meter to confirm they show the correct school. If not, restart the app and register again.

---

### Country not detected correctly

{% hint style="warning" %}
**What you'll see:** The detected country is wrong, or you see a message saying Giga Meter is not available in your country.
{% endhint %}

- **Wrong country detected:** Select the correct country from the dropdown, click **OK**, then **Confirm**.
- **Warning still appears after selecting the correct country:** This may be caused by a VPN or your IP address signalling a different location. You can proceed by clicking **Confirm**.
- **"Giga Meter is not available in \[country]":** Verify your country selection is correct. If the issue persists, contact your designated Giga focal point at UNICEF — the country may not yet be whitelisted on Giga's backend.

{% endtab %}

{% tab title="After installation" %}

### Tests not running or failing

{% hint style="warning" %}
**What you'll see:** Tests show as failed in the app, or no data appears on Giga Maps after several days.
{% endhint %}

Work through this checklist:

* [ ] Is the device **turned on** and not in Sleep mode?
* [ ] Is it connected to the **school's internet** (not a mobile hotspot or personal router)?
* [ ] Is it within the **measurement window** — 8 AM to 8 PM local time?
* [ ] Is the school's internet connection **working**? Test it by opening a website.

If all of the above are true and tests continue to fail, take a screenshot of the error shown in the app and send it to the administrator who guided your installation.

---

### School appears as "Unknown" on Giga Maps

{% hint style="warning" %}
**What you'll see:** The school is reporting data but appears labelled "Unknown" on Giga Maps.
{% endhint %}

The school ID used during registration may not match the ID in Giga's school database. Verify the school ID and contact the Giga team via your UNICEF focal point to correct the mapping.

---

### No data visible on Giga Maps after installation

Data takes up to **24–48 hours** to appear on Giga Maps after the first successful test. If nothing appears after 48 hours:

1. Open Giga Meter and check the Data tab — confirm at least one test shows as successful.
2. If no tests have run, work through the "Tests not running" checklist above.
3. If tests show as successful but Maps still shows no data, contact your focal point.

{% endtab %}
{% endtabs %}

---

## Still stuck?

For any issue not covered above: take a screenshot or copy the exact error message and send it to your focal point at the Ministry or at the UNICEF Country Office. They will escalate to Giga if needed.

* [FAQ](faq.md)
* [Installation Guide](../installation/installation-guide.md)
