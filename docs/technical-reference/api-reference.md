# API Reference

The Giga Meter API provides programmatic access to school registration records, country coverage, and individual connectivity measurements.

**Base URL:** `https://uni-ooi-giga-meter-backend.azurewebsites.net`

**Interactive explorer:** [maps.giga.global/docs/explore-api](https://maps.giga.global/docs/explore-api)

**Request access:** Contact the Giga team through your UNICEF country focal point. All endpoints require an API key.

---

## Authentication

All requests must include a Bearer token in the `Authorization` header:

```
Authorization: Bearer <your-api-key>
```

Requests without a valid token return `401 Unauthorized`.

---

## Endpoints

### Schools

`GET /api/v1/dailycheckapp_schools`

Returns the list of schools registered on the Giga Meter database.

**Parameters:**

| Name | Type | Description |
|---|---|---|
| `page` | number | Pages to skip before collecting results. If `page=2` and `size=10`, skips 20 records. Default: `0` |
| `size` | number | Number of schools to return. Default: `10` |
| `giga_id_school` | string | Filter by Giga school ID (UUID format, e.g. `2abb47dd-3fca-44b1-b6c8-0ec0c863c236`) |
| `country_iso3_code` | string | Filter by ISO3 country code (e.g. `IND`, `MDA`, `BRA`) |

**Example request:**

```
GET /api/v1/dailycheckapp_schools?size=1&country_iso3_code=ALB
Authorization: Bearer <your-api-key>
```

**Example response:**

```json
{
  "success": true,
  "data": [
    {
      "id": "11583751",
      "giga_id_school": "7c32006a-c3d1-3798-9082-be9b8222d872",
      "os": "windows",
      "app_version": "2.0.2",
      "country_code": "AL",
      "is_blocked": false,
      "created_at": "2026-06-17T07:45:14.976Z",
      "is_active": null,
      "wifi_connections": []
    }
  ],
  "timestamp": "2026-06-19T15:58:21.751Z",
  "message": "success"
}
```

**Key response fields:**

| Field | What it contains |
|---|---|
| `giga_id_school` | Giga's internal school UUID — use this to query measurements for a specific school |
| `os` | Operating system running Giga Meter at this device |
| `app_version` | Giga Meter version installed |
| `country_code` | ISO2 country code of the registered school |
| `is_blocked` | Whether the device has been blocked by the backend |
| `created_at` | Timestamp of initial registration |

---

### Countries

`GET /api/v1/dailycheckapp_countries`

Returns the list of countries with at least one registered Giga Meter school.

**Parameters:**

| Name | Type | Description |
|---|---|---|
| `page` | number | Pages to skip. Default: `0` |
| `size` | number | Number of countries to return. Default: `10` |

**Example request:**

```
GET /api/v1/dailycheckapp_countries?size=10
Authorization: Bearer <your-api-key>
```

**Example response:**

```json
{
  "success": true,
  "data": [
    {
      "id": "44",
      "code": "AL",
      "code_iso3": "ALB",
      "name": "Albania",
      "country_id": "178",
      "created_at": "2026-02-16T12:36:39.529Z"
    }
  ],
  "timestamp": "2026-06-19T15:58:21.966Z",
  "message": "success"
}
```

**Key response fields:**

| Field | What it contains |
|---|---|
| `code` | ISO2 country code |
| `code_iso3` | ISO3 country code — use this as `country_iso3_code` in Schools and Measurements queries |
| `name` | Country name |

---

### Measurements

`GET /api/v1/measurements`

Returns individual Giga Meter test results. Each record is one speed test run at one school at one point in time.

**Parameters:**

| Name | Type | Description |
|---|---|---|
| `page` | number | Pages to skip. Default: `0` |
| `size` | number | Records per page. Min: `1`, max: `100`. Default: `10` |
| `orderBy` | string | Column to sort by. Pass `created_at` for ASC, `-created_at` for DESC. Default: `-timestamp` |
| `giga_id_school` | string | Filter by Giga school UUID |
| `country_iso3_code` | string | Filter by ISO3 country code |
| `filterBy` | string | Column to filter on (e.g. `timestamp`, `created_at`) |
| `filterCondition` | string | Comparison operator: `lt`, `lte`, `gt`, `gte`, `eq` |
| `filterValue` | string | Value to compare against (e.g. `2024-01-14` or `2024-01-14T15:13:30.824Z`) |

**Example request — last 5 measurements for a specific school:**

```
GET /api/v1/measurements?size=5&giga_id_school=7c32006a-c3d1-3798-9082-be9b8222d872&orderBy=-timestamp
Authorization: Bearer <your-api-key>
```

**Example request — all measurements after a given date:**

```
GET /api/v1/measurements?filterBy=timestamp&filterCondition=gt&filterValue=2024-06-01T00:00:00.000Z&country_iso3_code=MDA
Authorization: Bearer <your-api-key>
```

**Example response:**

```json
{
  "success": true,
  "data": [
    {
      "id": "7179786",
      "Timestamp": "2026-06-17T14:30:44.369Z",
      "DeviceType": "windows",
      "Notes": "daily",
      "ClientInfo": {
        "ASN": "AS60471",
        "ISP": "AS60471 Mobitel sh.p.k.",
        "City": "Kashar",
        "Region": "Tirana",
        "Country": "AL",
        "Latitude": 41.3497,
        "Longitude": 19.7103,
        "Timezone": "Europe/Tirane"
      },
      "ServerInfo": {
        "City": "Podgorica",
        "FQDN": "ndt-iupui-mlab1-tgd01.mlab-oti.measurement-lab.org",
        "Country": "ME",
        "Metro": "tgd"
      },
      "Download": 93346.08,
      "Upload": 31959.84,
      "Latency": 5
    }
  ],
  "timestamp": "2026-06-19T15:58:22.000Z",
  "message": "success"
}
```

**Key response fields:**

| Field | Unit | What it contains |
|---|---|---|
| `Timestamp` | — | When the measurement was taken (ISO 8601) |
| `DeviceType` | — | Operating system of the measuring device |
| `Notes` | — | Measurement trigger type (`daily` = scheduled; `manual` = user-triggered) |
| `ClientInfo.ASN` | — | Autonomous System Number of the school's internet provider |
| `ClientInfo.ISP` | — | Human-readable ISP name |
| `ClientInfo.Country` | — | ISO2 country code where the client IP is geolocated |
| `ServerInfo.City` | — | Location of the M-Lab NDT server used for this test |
| `Download` | Kbps | Download throughput measured by this test |
| `Upload` | Kbps | Upload throughput measured by this test |
| `Latency` | ms | Round-trip latency measured by this test |

{% hint style="info" %}
`Download` and `Upload` values are in **Kbps**. Divide by 1000 to convert to Mbps (e.g. 93346 Kbps = 93.3 Mbps).
{% endhint %}

---

## Pagination

All endpoints use offset-based pagination via `page` and `size`.

| To get | Use |
|---|---|
| First 10 records | `page=0&size=10` |
| Next 10 records | `page=1&size=10` |
| Records 21–30 | `page=2&size=10` |

The `data` array in each response contains exactly `size` records (or fewer if you've reached the end of the dataset). There is no total count field — iterate until `data` returns an empty array.

---

## Date filtering

Use `filterBy`, `filterCondition`, and `filterValue` together on the Measurements endpoint to query by time range:

```
GET /api/v1/measurements
  ?filterBy=timestamp
  &filterCondition=gt
  &filterValue=2024-01-01T00:00:00.000Z
  &country_iso3_code=MDA
  &size=100
  &orderBy=timestamp
```

Accepted `filterCondition` values: `lt` (less than), `lte` (less than or equal), `gt` (greater than), `gte` (greater than or equal), `eq` (equal).

Date values can be passed as `YYYY-MM-DD` or full ISO 8601 timestamps (`YYYY-MM-DDTHH:MM:SS.sssZ`).

---

## Response envelope

Every response follows the same envelope:

```json
{
  "success": true,
  "data": [ ... ],
  "timestamp": "2026-06-19T15:58:21.751Z",
  "message": "success"
}
```

On error, `success` is `false` and `message` contains a description of the problem.

---

## Related pages

- [Privacy & Security](../security/privacy-and-security.md)
- [Network Destinations & Firewall Configuration](../security/network-destinations.md)
- [Data Governance & Privacy](data-governance.md)
- [Metric Glossary](metric-glossary.md)
