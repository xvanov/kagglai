# Current Understanding

> Living document capturing the team's shared mental model of the data, problem, and effective approaches.

## Problem Understanding

**Goal**: Determine conditions that cause water intrusion through wall outlets in a San Francisco home.

**Wall Flood Events** (confirmed, with full weather data):
| Date | Daily Precip | 7-day Precip | Wind Gusts | Wind Dir | Dry Spell | Mechanism |
|------|--------------|--------------|------------|----------|-----------|-----------|
| Dec 31, 2022 | 5.46 in | 8.85 in | 42 km/h | NW (307°) | 0 days | VOLUME |
| Nov 13, 2025 | 1.28 in | 1.28 in | 64 km/h | S (172°) | 7 days | DRY-SPELL |
| Dec 24, 2025 | 0.73 in | 3.09 in | 82 km/h | SSE (165°) | 0 days | WIND-DRIVEN |
| Dec 26, 2025 | 0.43 in | 3.13 in | 72 km/h | SSW (205°) | 1 day | WIND-DRIVEN |

**Oct 13, 2025 Ceiling Leak** (NOT wall outlet):
- Daily: 0.75 in, 7-day: 0.75 in
- Gusts: 60 km/h, Direction: SW (235°)
- Does NOT meet any flood mechanism criteria
- **Confirmed**: NOT precipitation-related - investigate plumbing/HVAC

## Three Flooding Mechanisms Discovered

### Mechanism 1: VOLUME OVERLOAD
```
Daily precipitation > 4 inches  OR  7-day precipitation > 7 inches
```
- **Example**: Dec 31, 2022 (5.46 in/day, 8.85 in/7-day)
- **Wind**: Not a factor (NW direction, average gusts)
- **Theory**: Sheer water volume exceeds wall's drainage capacity

### Mechanism 2: WIND-DRIVEN (High Intensity)
```
Southerly wind (90-220°)  AND  Gusts >= 70 km/h  AND  7-day precip >= 3 inches
```
- **Example**: Dec 24-26, 2025 (72-82 km/h gusts, only ~3 in rain)
- **Theory**: Extreme gusts drive rain horizontally INTO the wall

### Mechanism 3: DRY-SPELL VULNERABILITY
```
Daily precip >= 1 inch  AND  Southerly wind  AND  Gusts >= 60 km/h  AND  Dry spell >= 7 days
```
- **Example**: Nov 13, 2025 (1.28 in after 7 dry days, 64 km/h gusts)
- **Theory**: After extended dry period, wall/building more vulnerable (cracks, dried seals, debris in drainage?)

## Predictive Model Performance

**FLOOD RISK = HIGH** when ANY mechanism condition is met.

| Metric | Value |
|--------|-------|
| Floods detected | 4/4 (100% recall) |
| False positive days | 12 over 4 years |
| False positive storm events | 5 distinct events |

### False Positive Analysis

| Storm Period | Mechanism Triggered | Notes |
|--------------|---------------------|-------|
| Jan 1-6, 2023 | VOLUME | Same storm as Dec 31 flood - expected |
| Jan 9-10, 2023 | WIND-DRIVEN | **Investigate**: undetected intrusion? |
| Feb 4, 2024 | WIND-DRIVEN | **Investigate**: undetected intrusion? |
| Feb 4-6, 2025 | WIND-DRIVEN | **Investigate**: undetected intrusion? |
| Dec 25, 2025 | WIND-DRIVEN | Between Dec 24 and 26 floods - expected |

**Key Finding**: The "false positives" on Jan 9-10, 2023, Feb 2024, and Feb 2025 had very similar conditions to actual floods. Check for any signs of past water damage during these dates.

## Key Comparisons

### Why Nov 13, 2025 flooded but Jan 31, 2024 didn't:
| Factor | Nov 13, 2025 (FLOOD) | Jan 31, 2024 (no flood) |
|--------|---------------------|------------------------|
| Daily precip | 1.28 in | 1.67 in |
| Dry spell | **7 days** | 6 days |
| Gusts | **64 km/h** | 55 km/h |
| Direction | S (172°) | SSE (155°) |

The combination of longer dry spell AND higher gusts appears to be the threshold.

### Why Dec 24-26, 2025 flooded with less rain than Dec 2022:
| Factor | Dec 31, 2022 | Dec 24-26, 2025 |
|--------|--------------|-----------------|
| 7-day precip | 8.85 in | 3.1 in |
| Daily precip | 5.46 in | 0.4-0.7 in |
| Gusts | 42 km/h (40th %ile) | 72-82 km/h (98-99th %ile) |
| Wind dir | NW (307°) | SSE/SSW (165-205°) |

**65% less rain but twice the gusts from the ocean direction** = different mechanism entirely.

## Data Sources

### Precipitation Data
- **File**: `_kagglai/data/sf_downtown_precipitation_USW00023272.csv`
- **Source**: NOAA GHCN-Daily, Downtown SF station USW00023272
- **Coverage**: 1921-2026 (104 years, 38,363 records)

### Wind Data
- **File**: `_kagglai/data/sf_wind_daily_2022_2026.csv`
- **Source**: Open-Meteo Historical Weather API (reanalysis data)
- **Coverage**: Jan 2022 - Jan 2026 (complete)
- **Fields**: wind_speed_max_kmh, wind_direction_dominant_deg, wind_gusts_max_kmh
- **API**: `https://archive-api.open-meteo.com/v1/archive` (free, no key required)

## Open Questions

1. **Wall orientation**: Does the leaking wall face S/SE/SSW (toward ocean)? This would confirm the wind-driven mechanism.
2. **Unrecorded floods**: Check for any water damage signs from Jan 9-10 2023, Feb 2024, Feb 2025 storms.
3. **Dry-spell mechanism**: Why does a 7+ day dry spell increase vulnerability? Possible causes:
   - Dried/cracked sealant around outlets
   - Debris accumulation in drainage channels
   - Building material contraction
4. **Remediation priorities**:
   - For VOLUME floods: Improve drainage capacity
   - For WIND-DRIVEN floods: Weatherproof the south-facing exterior wall
   - For DRY-SPELL floods: Regular maintenance after dry periods?

## Key Files

- `_kagglai/data/sf_downtown_precipitation_USW00023272.csv` - 104 years precipitation
- `_kagglai/data/sf_wind_daily_2022_2026.csv` - 4 years daily wind data

---

*Last updated: January 18, 2026*
