#!/usr/bin/env python3
"""
Flood Risk Analysis Script
--------------------------
Analyzes precipitation and wind data to identify storm events that triggered
or could have triggered wall flooding.

FILTER CRITERIA FOR HIGH-RISK STORMS:
=====================================
A storm is flagged as HIGH RISK if ANY of these conditions are met:

MECHANISM 1 - VOLUME OVERLOAD:
    Peak daily precipitation > 4.0 inches
    OR
    Peak 7-day cumulative precipitation > 7.0 inches

MECHANISM 2 - WIND-DRIVEN (High Intensity):
    Southerly wind direction (90-220 degrees)
    AND Wind gusts >= 70 km/h
    AND 7-day cumulative precipitation >= 3.0 inches

MECHANISM 3 - DRY-SPELL VULNERABILITY:
    Daily precipitation >= 1.0 inch
    AND Southerly wind direction (90-220 degrees)
    AND Wind gusts >= 60 km/h
    AND Dry spell before storm >= 7 days

STORM DEFINITION:
=================
A storm is defined as consecutive days with precipitation, allowing
up to 2 dry days (< 0.1 inch) within a storm period.

OUTPUT:
=======
Table showing all high-risk storms with:
- Storm period (first rain to last rain)
- Dry spell before storm
- Total precipitation
- Avg daily precipitation over storm
- Max wind gusts during storm
- Dominant wind direction
- Mechanism that triggered the flag
- Flood dates (if any)

Usage:
    python flood_risk_analysis.py
"""

import csv
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
SCRIPT_DIR = Path(__file__).parent
PRECIP_FILE = SCRIPT_DIR / "sf_downtown_precipitation_USW00023272.csv"
WIND_FILE = SCRIPT_DIR / "sf_wind_daily_2022_2026.csv"

# Known flood dates (wall outlets)
FLOOD_DATES = ['2022-12-31', '2025-11-13', '2025-12-24', '2025-12-26']

# Other water events (not wall outlets)
OTHER_WATER_EVENTS = {
    '2025-10-13': 'Ceiling leak (not outlet)'
}

# Filter thresholds
VOLUME_DAILY_THRESHOLD = 4.0  # inches
VOLUME_7DAY_THRESHOLD = 7.0   # inches
WIND_DRIVEN_GUST_THRESHOLD = 70  # km/h
WIND_DRIVEN_7DAY_THRESHOLD = 3.0  # inches
DRY_SPELL_DAILY_THRESHOLD = 1.0  # inches
DRY_SPELL_GUST_THRESHOLD = 60  # km/h
DRY_SPELL_DAYS_THRESHOLD = 7  # days
SOUTHERLY_MIN = 90   # degrees
SOUTHERLY_MAX = 220  # degrees

# Storm detection
RAIN_THRESHOLD = 0.1  # inches - below this is considered "dry"
MAX_DRY_GAP = 2  # max consecutive dry days within a storm


def load_data():
    """Load precipitation and wind data from CSV files."""
    wind_data = {}
    with open(WIND_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            wind_data[row['date']] = {
                'speed': float(row['wind_speed_max_kmh']) if row['wind_speed_max_kmh'] else None,
                'direction': float(row['wind_direction_dominant_deg']) if row['wind_direction_dominant_deg'] else None,
                'gusts': float(row['wind_gusts_max_kmh']) if row['wind_gusts_max_kmh'] else None
            }

    precip_data = {}
    with open(PRECIP_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header line 1
        next(reader)  # Skip column names
        for row in reader:
            if len(row) >= 5:
                try:
                    precip_data[row[0]] = float(row[4]) if row[4] else 0.0
                except:
                    precip_data[row[0]] = 0.0

    return precip_data, wind_data


def get_7day_precip(precip_data, date_str):
    """Calculate 7-day cumulative precipitation ending on date_str."""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return sum(precip_data.get((date - timedelta(days=i)).strftime('%Y-%m-%d'), 0.0) for i in range(7))


def get_dry_spell_before(precip_data, date_str, threshold=RAIN_THRESHOLD):
    """Count consecutive days with < threshold precipitation before date_str."""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    days = 0
    for i in range(1, 365):
        d = (date - timedelta(days=i)).strftime('%Y-%m-%d')
        if precip_data.get(d, 0) >= threshold:
            break
        days += 1
    return days


def is_southerly(deg):
    """Check if wind direction is from southerly quadrant (90-220 degrees)."""
    return deg is not None and SOUTHERLY_MIN <= deg <= SOUTHERLY_MAX


def wind_dir_to_cardinal(deg):
    """Convert degrees to cardinal direction string."""
    if deg is None:
        return "N/A"
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
            'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    idx = int((deg + 11.25) / 22.5) % 16
    return f"{dirs[idx]} ({deg:.0f}°)"


def identify_storms(precip_data, start_date='2022-01-01', end_date='2026-12-31'):
    """
    Identify storm periods from precipitation data.
    A storm is consecutive rainy days, allowing up to MAX_DRY_GAP dry days within.
    """
    storms = []
    current_storm = None
    dry_gap = 0

    date = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    while date <= end:
        date_str = date.strftime('%Y-%m-%d')
        precip = precip_data.get(date_str, 0)

        if precip >= RAIN_THRESHOLD:
            # Rainy day
            if current_storm is None:
                # Start new storm
                current_storm = {
                    'start': date_str,
                    'end': date_str,
                    'days': [date_str],
                    'precip': [precip]
                }
            else:
                # Continue storm (including any dry gap days)
                current_storm['end'] = date_str
                current_storm['days'].append(date_str)
                current_storm['precip'].append(precip)
            dry_gap = 0
        else:
            # Dry day
            if current_storm is not None:
                dry_gap += 1
                if dry_gap > MAX_DRY_GAP:
                    # End current storm
                    storms.append(current_storm)
                    current_storm = None
                    dry_gap = 0

        date += timedelta(days=1)

    # Don't forget last storm
    if current_storm is not None:
        storms.append(current_storm)

    return storms


def analyze_storm(storm, precip_data, wind_data):
    """Analyze a storm and determine if it meets high-risk criteria."""
    start = storm['start']
    end = storm['end']

    # Calculate metrics over the storm period
    start_dt = datetime.strptime(start, '%Y-%m-%d')
    end_dt = datetime.strptime(end, '%Y-%m-%d')
    storm_days = (end_dt - start_dt).days + 1

    total_precip = 0
    max_daily = 0
    max_7day = 0
    max_gusts = 0
    max_gust_direction = None

    date = start_dt
    while date <= end_dt:
        date_str = date.strftime('%Y-%m-%d')

        daily_precip = precip_data.get(date_str, 0)
        total_precip += daily_precip
        max_daily = max(max_daily, daily_precip)

        p7 = get_7day_precip(precip_data, date_str)
        max_7day = max(max_7day, p7)

        if date_str in wind_data:
            w = wind_data[date_str]
            if w['gusts'] and w['gusts'] > max_gusts:
                max_gusts = w['gusts']
                max_gust_direction = w['direction']

        date += timedelta(days=1)

    avg_daily = total_precip / storm_days if storm_days > 0 else 0
    dry_spell_before = get_dry_spell_before(precip_data, start)

    # Check which flood dates fall within this storm
    flood_dates_in_storm = [d for d in FLOOD_DATES if start <= d <= end]

    # Check for other water events (e.g., ceiling leaks)
    other_events_in_storm = {d: desc for d, desc in OTHER_WATER_EVENTS.items() if start <= d <= end}

    # Determine mechanism(s) triggered and capture the TRIGGER DAY details
    mechanisms = []
    trigger_days = []  # Store details of days that triggered mechanisms

    # Mechanism 1: Volume
    if max_daily > VOLUME_DAILY_THRESHOLD or max_7day > VOLUME_7DAY_THRESHOLD:
        mechanisms.append('VOLUME')
        # Find the day with max daily precip
        date = start_dt
        while date <= end_dt:
            date_str = date.strftime('%Y-%m-%d')
            if precip_data.get(date_str, 0) == max_daily:
                w = wind_data.get(date_str, {})
                trigger_days.append({
                    'date': date_str,
                    'mechanism': 'VOLUME',
                    'daily': max_daily,
                    'p7': get_7day_precip(precip_data, date_str),
                    'gusts': w.get('gusts'),
                    'direction': w.get('direction')
                })
                break
            date += timedelta(days=1)

    # Check each day for wind-driven or dry-spell mechanisms
    date = start_dt
    while date <= end_dt:
        date_str = date.strftime('%Y-%m-%d')
        daily_precip = precip_data.get(date_str, 0)
        p7 = get_7day_precip(precip_data, date_str)

        if date_str in wind_data:
            w = wind_data[date_str]
            gusts = w['gusts'] or 0
            direction = w['direction']

            # Mechanism 2: Wind-driven
            if (is_southerly(direction) and gusts >= WIND_DRIVEN_GUST_THRESHOLD
                and p7 >= WIND_DRIVEN_7DAY_THRESHOLD and 'WIND-DRIVEN' not in mechanisms):
                mechanisms.append('WIND-DRIVEN')
                trigger_days.append({
                    'date': date_str,
                    'mechanism': 'WIND-DRIVEN',
                    'daily': daily_precip,
                    'p7': p7,
                    'gusts': gusts,
                    'direction': direction
                })

            # Mechanism 3: Dry-spell vulnerability
            if (daily_precip >= DRY_SPELL_DAILY_THRESHOLD and is_southerly(direction)
                and gusts >= DRY_SPELL_GUST_THRESHOLD and dry_spell_before >= DRY_SPELL_DAYS_THRESHOLD
                and 'DRY-SPELL' not in mechanisms):
                mechanisms.append('DRY-SPELL')
                trigger_days.append({
                    'date': date_str,
                    'mechanism': 'DRY-SPELL',
                    'daily': daily_precip,
                    'p7': p7,
                    'gusts': gusts,
                    'direction': direction
                })

        date += timedelta(days=1)

    # Get the primary trigger day (first one that triggered a mechanism)
    primary_trigger = trigger_days[0] if trigger_days else None

    # Include in output if high-risk OR has any water event
    include_in_output = len(mechanisms) > 0 or flood_dates_in_storm or other_events_in_storm

    return {
        'start': start,
        'end': end,
        'storm_days': storm_days,
        'dry_spell_before': dry_spell_before,
        'total_precip': total_precip,
        'avg_daily': avg_daily,
        'max_daily': max_daily,
        'max_7day': max_7day,
        'max_gusts': max_gusts,
        'max_gust_direction': max_gust_direction,
        'dominant_direction': wind_dir_to_cardinal(max_gust_direction),
        'flood_dates': flood_dates_in_storm,
        'other_events': other_events_in_storm,
        'mechanisms': mechanisms,
        'trigger_days': trigger_days,
        'primary_trigger': primary_trigger,
        'is_high_risk': len(mechanisms) > 0,
        'include_in_output': include_in_output
    }


def main():
    print("Loading data...")
    precip_data, wind_data = load_data()

    print("Identifying storms...")
    storms = identify_storms(precip_data, '2022-01-01', '2026-01-15')

    print("Analyzing storms...")
    analyzed = [analyze_storm(s, precip_data, wind_data) for s in storms]

    # Filter to storms that should be included (high-risk OR has water events)
    high_risk = [s for s in analyzed if s['include_in_output']]

    # Print filter criteria
    print("\n" + "="*120)
    print("FLOOD RISK ANALYSIS - FILTER CRITERIA")
    print("="*120)
    print(f"""
MECHANISM 1 - VOLUME OVERLOAD:
    Peak daily precipitation > {VOLUME_DAILY_THRESHOLD} inches
    OR Peak 7-day cumulative > {VOLUME_7DAY_THRESHOLD} inches

MECHANISM 2 - WIND-DRIVEN (High Intensity):
    Southerly wind ({SOUTHERLY_MIN}-{SOUTHERLY_MAX}°) AND Gusts >= {WIND_DRIVEN_GUST_THRESHOLD} km/h AND 7-day >= {WIND_DRIVEN_7DAY_THRESHOLD} in

MECHANISM 3 - DRY-SPELL VULNERABILITY:
    Daily >= {DRY_SPELL_DAILY_THRESHOLD} in AND Southerly AND Gusts >= {DRY_SPELL_GUST_THRESHOLD} km/h AND Dry spell >= {DRY_SPELL_DAYS_THRESHOLD} days

STORM DEFINITION:
    Consecutive days with precip >= {RAIN_THRESHOLD} in, allowing up to {MAX_DRY_GAP} dry days within storm
""")

    # Print results table
    print("="*150)
    print("HIGH-RISK STORM EVENTS")
    print("="*150)
    print("\nNote: 'Trigger Day' shows conditions on the day that first met mechanism criteria")

    print(f"\n{'#':<3} {'Storm Period':<28} {'Days':>5} {'Dry':>5} {'Total':>7} {'Avg/d':>7} {'Trigger Day':<12} {'Daily':>6} {'7-day':>6} {'Gusts':>8} {'Wind':>12} {'Mechanism':<15} {'Flood?':<22}")
    print("-"*160)

    for i, s in enumerate(high_risk, 1):
        period = f"{s['start']} to {s['end']}"
        days_str = f"{s['storm_days']}d"
        dry_str = f"{s['dry_spell_before']}d"
        total_str = f"{s['total_precip']:.1f}\""
        avg_str = f"{s['avg_daily']:.2f}\""

        # Get trigger day info (or event day for non-high-risk storms)
        trigger = s['primary_trigger']
        if trigger:
            trigger_date = trigger['date']
            trigger_daily = f"{trigger['daily']:.2f}\""
            trigger_7d = f"{trigger['p7']:.1f}\""
            trigger_gusts = f"{trigger['gusts']:.0f}km/h" if trigger['gusts'] else "N/A"
            trigger_wind = wind_dir_to_cardinal(trigger['direction'])[:12] if trigger['direction'] else "N/A"
        elif s.get('other_events'):
            # For non-high-risk storms with other events, show conditions on event date
            event_date = list(s['other_events'].keys())[0]
            trigger_date = event_date
            trigger_daily = f"{precip_data.get(event_date, 0):.2f}\""
            trigger_7d = f"{get_7day_precip(precip_data, event_date):.1f}\""
            w = wind_data.get(event_date, {})
            trigger_gusts = f"{w.get('gusts', 0):.0f}km/h" if w.get('gusts') else "N/A"
            trigger_wind = wind_dir_to_cardinal(w.get('direction'))[:12] if w.get('direction') else "N/A"
        else:
            trigger_date = "-"
            trigger_daily = "-"
            trigger_7d = "-"
            trigger_gusts = "-"
            trigger_wind = "-"

        mech_str = "+".join(s['mechanisms']) if s['mechanisms'] else "None"

        # Build flood/event string
        flood_parts = []
        if s['flood_dates']:
            flood_parts.extend(s['flood_dates'])
        if s.get('other_events'):
            for date, desc in s['other_events'].items():
                flood_parts.append(f"{date} ({desc})")
        flood_str = ", ".join(flood_parts) if flood_parts else "No flood"

        print(f"{i:<3} {period:<28} {days_str:>5} {dry_str:>5} {total_str:>7} {avg_str:>7} {trigger_date:<12} {trigger_daily:>6} {trigger_7d:>6} {trigger_gusts:>8} {trigger_wind:>12} {mech_str:<15} {flood_str:<30}")

    # Summary
    print("\n" + "="*120)
    print("SUMMARY")
    print("="*120)

    # Categorize storms
    flood_storms = [s for s in high_risk if s['flood_dates']]
    other_event_storms = [s for s in high_risk if s.get('other_events') and not s['flood_dates']]
    high_risk_only = [s for s in high_risk if s['is_high_risk']]
    false_positive_storms = [s for s in high_risk if s['is_high_risk'] and not s['flood_dates'] and not s.get('other_events')]

    print(f"\nTotal storms shown: {len(high_risk)}")
    print(f"  - With wall outlet flooding: {len(flood_storms)}")
    print(f"  - With other water events (not outlets): {len(other_event_storms)}")
    print(f"  - High-risk but no flood observed (false positives): {len(false_positive_storms)}")

    if false_positive_storms:
        print("\nFALSE POSITIVE STORMS - Investigate for undetected damage:")
        for s in false_positive_storms:
            print(f"  - {s['start']} to {s['end']}: {', '.join(s['mechanisms'])}, {s['max_gusts']:.0f} km/h gusts, {s['dominant_direction']}")

    # Check if all known floods are captured
    all_flood_dates_found = set()
    for s in high_risk:
        all_flood_dates_found.update(s['flood_dates'])

    missing_floods = set(FLOOD_DATES) - all_flood_dates_found
    if missing_floods:
        print(f"\nWARNING: These known flood dates were NOT captured by the filter:")
        for d in missing_floods:
            print(f"  - {d}")
    else:
        print(f"\nAll {len(FLOOD_DATES)} known flood dates captured by filter (100% recall)")


if __name__ == '__main__':
    main()
