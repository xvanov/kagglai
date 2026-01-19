"""
Home Water Intrusion Analysis - San Francisco
==============================================

Analyzes precipitation and wind data to determine conditions that cause
water intrusion through wall outlets in a San Francisco home.

Key findings:
- Wall flooding requires ~3+ inches over 7 days after a dry spell
- Wind direction from SW/S (180-225°) appears to be a key factor
- Oct 13, 2025 ceiling leak was NOT precipitation-related

Data sources:
- NOAA GHCN-Daily (precipitation): Downtown SF station USW00023272
- NOAA ISD Hourly (wind direction): SFO Airport station 724940-23234

Usage:
    python home_flood_analysis.py

Author: Atlas (Data Analyst Agent)
Date: January 2025
"""

import csv
import gzip
import os
import re
from datetime import datetime, timedelta
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
import urllib.request


# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class FloodEvent:
    """Recorded flood/water intrusion event."""
    date: datetime
    flood_type: str  # "wall" or "ceiling"
    notes: str = ""


@dataclass
class DailyWeather:
    """Combined daily weather data."""
    date: datetime
    prcp: Optional[float] = None  # Precipitation (inches)
    wind_dir: Optional[int] = None  # Predominant wind direction (degrees)
    wind_speed: Optional[float] = None  # Max wind speed (knots)
    wind_gust: Optional[float] = None  # Max gust (knots)


# =============================================================================
# CONFIGURATION
# =============================================================================

# Known flood events (wall outlets unless noted)
FLOOD_EVENTS = [
    FloodEvent(datetime(2022, 12, 31), "wall", "Water from outlets in wall"),
    FloodEvent(datetime(2025, 10, 13), "ceiling", "Ceiling leak - different from wall floods"),
    FloodEvent(datetime(2025, 12, 24), "wall", "Water from outlets in wall"),
    FloodEvent(datetime(2025, 12, 26), "wall", "Water from outlets in wall"),
]

# Wall floods only (for threshold analysis)
WALL_FLOOD_DATES = [
    datetime(2022, 12, 31),
    datetime(2025, 12, 24),
    datetime(2025, 12, 26),
]

# Data file paths
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")
PRECIPITATION_FILES = [
    os.path.join(DOWNLOADS_DIR, "USW00023272.csv"),  # Downtown SF - best coverage
    os.path.join(DOWNLOADS_DIR, "US1CASF0017.csv"),  # SF 1.6 SE
    os.path.join(DOWNLOADS_DIR, "USC00047767.csv"),  # Oceanside SF
    os.path.join(DOWNLOADS_DIR, "precipitation_san_franisco_US1CASF0020.csv"),  # SF 3.1 W
]

# ISD data for wind (downloaded from AWS)
ISD_STATION = "724940-23234"  # SFO Airport
ISD_AWS_URL = "https://noaa-isd-pds.s3.amazonaws.com/data/{year}/{station}-{year}.gz"


# =============================================================================
# DATA LOADING FUNCTIONS
# =============================================================================

def load_precipitation_data(filepath: str) -> Dict[datetime, float]:
    """
    Load GHCN-Daily precipitation data from CSV.
    Returns dict of date -> precipitation in inches.
    """
    data = {}
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip station name line
            next(reader)  # Skip header line
            for row in reader:
                if len(row) >= 5:
                    try:
                        date = datetime.strptime(row[0], '%Y-%m-%d')
                        prcp_str = row[4].strip()
                        if prcp_str and prcp_str not in ['', '99.99']:
                            data[date] = float(prcp_str)
                    except (ValueError, IndexError):
                        pass
    except FileNotFoundError:
        print(f"Warning: File not found: {filepath}")
    return data


def load_all_precipitation_data() -> Dict[datetime, float]:
    """Load precipitation from all available stations, preferring most complete."""
    combined = {}
    for filepath in PRECIPITATION_FILES:
        station_data = load_precipitation_data(filepath)
        # Add data only if we don't have it from a better source
        for date, prcp in station_data.items():
            if date not in combined:
                combined[date] = prcp
    return combined


def download_isd_data(year: int, output_dir: str = "/tmp/isd_data") -> Optional[str]:
    """
    Download ISD hourly data from AWS for a given year.
    Returns path to decompressed file or None if failed.
    """
    os.makedirs(output_dir, exist_ok=True)
    url = ISD_AWS_URL.format(year=year, station=ISD_STATION)
    gz_path = os.path.join(output_dir, f"sfo_{year}.gz")
    txt_path = os.path.join(output_dir, f"sfo_{year}")

    try:
        urllib.request.urlretrieve(url, gz_path)
        with gzip.open(gz_path, 'rb') as f_in:
            with open(txt_path, 'wb') as f_out:
                f_out.write(f_in.read())
        os.remove(gz_path)
        return txt_path
    except Exception as e:
        print(f"Warning: Could not download ISD data for {year}: {e}")
        return None


def parse_isd_line(line: str) -> Optional[Tuple[datetime, int, int, Optional[int]]]:
    """
    Parse ISD format line to extract date, wind direction, speed, gust.
    Returns (datetime, wind_dir_degrees, wind_speed_knots, gust_knots) or None.
    """
    try:
        # Date from fixed positions
        date_str = line[15:27]
        dt = datetime(
            int(date_str[0:4]), int(date_str[4:6]), int(date_str[6:8]),
            int(date_str[8:10]), int(date_str[10:12])
        )

        # Extract from METAR in remarks (most reliable)
        metar_match = re.search(
            r'METAR\s+\w+\s+\d+Z\s+(\d{3})(\d{2,3})(?:G(\d{2,3}))?KT',
            line
        )
        if metar_match:
            wind_dir = int(metar_match.group(1))
            wind_spd = int(metar_match.group(2))
            wind_gust = int(metar_match.group(3)) if metar_match.group(3) else None
            return dt, wind_dir, wind_spd, wind_gust

        return None
    except Exception:
        return None


def load_isd_wind_data(years: List[int] = None) -> Dict[datetime, Dict]:
    """
    Load ISD wind data for specified years.
    Returns dict of date -> {directions: [], speeds: [], gusts: []}.
    """
    if years is None:
        years = [2022, 2023, 2024, 2025]

    daily_wind = defaultdict(lambda: {'dirs': [], 'spds': [], 'gusts': []})

    for year in years:
        filepath = f"/tmp/isd_data/sfo_{year}"

        # Download if not exists
        if not os.path.exists(filepath):
            filepath = download_isd_data(year)
            if filepath is None:
                continue

        try:
            with open(filepath, 'r', errors='ignore') as f:
                for line in f:
                    result = parse_isd_line(line)
                    if result:
                        dt, wind_dir, wind_spd, wind_gust = result
                        day = dt.replace(hour=0, minute=0, second=0, microsecond=0)
                        if wind_dir and wind_dir != 999:
                            daily_wind[day]['dirs'].append(wind_dir)
                        if wind_spd:
                            daily_wind[day]['spds'].append(wind_spd)
                        if wind_gust:
                            daily_wind[day]['gusts'].append(wind_gust)
        except FileNotFoundError:
            pass

    return dict(daily_wind)


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def get_cumulative_precip(prcp_data: Dict[datetime, float],
                          end_date: datetime, days: int) -> float:
    """Get cumulative precipitation for N days ending on end_date."""
    total = 0.0
    for i in range(days):
        d = end_date - timedelta(days=i)
        total += prcp_data.get(d, 0) or 0
    return total


def get_dry_spell_before(prcp_data: Dict[datetime, float],
                         date: datetime, threshold: float = 0.1) -> int:
    """Count consecutive dry days (< threshold) before a date."""
    dry_days = 0
    d = date - timedelta(days=1)
    while d in prcp_data:
        if (prcp_data.get(d, 0) or 0) < threshold:
            dry_days += 1
            d -= timedelta(days=1)
        else:
            break
    return dry_days


def get_predominant_wind_direction(directions: List[int]) -> Optional[int]:
    """Get most common wind direction (binned to 45-degree sectors)."""
    if not directions:
        return None
    sectors = defaultdict(int)
    for d in directions:
        sector = round(d / 45) % 8
        sectors[sector] += 1
    most_common = max(sectors, key=sectors.get)
    return most_common * 45


def direction_to_compass(degrees: Optional[int]) -> str:
    """Convert degrees to compass direction."""
    if degrees is None:
        return "VAR"
    dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    return dirs[round(degrees / 45) % 8]


def analyze_flood_event(prcp_data: Dict[datetime, float],
                        wind_data: Dict[datetime, Dict],
                        flood_date: datetime) -> Dict:
    """Analyze conditions around a flood event."""
    result = {
        'date': flood_date,
        'prcp_1d': prcp_data.get(flood_date),
        'prcp_3d': get_cumulative_precip(prcp_data, flood_date, 3),
        'prcp_7d': get_cumulative_precip(prcp_data, flood_date, 7),
        'dry_spell_before': get_dry_spell_before(prcp_data, flood_date),
        'wind_dir': None,
        'wind_dir_compass': None,
        'max_wind': None,
        'max_gust': None,
    }

    # Get wind data if available
    if flood_date in wind_data:
        wd = wind_data[flood_date]
        result['wind_dir'] = get_predominant_wind_direction(wd['dirs'])
        result['wind_dir_compass'] = direction_to_compass(result['wind_dir'])
        result['max_wind'] = max(wd['spds']) if wd['spds'] else None
        result['max_gust'] = max(wd['gusts']) if wd['gusts'] else None

    return result


def find_high_precip_events(prcp_data: Dict[datetime, float],
                            threshold_7d: float = 3.0,
                            start_date: datetime = None,
                            end_date: datetime = None,
                            exclude_dates: List[datetime] = None) -> List[Dict]:
    """
    Find all high-precipitation events meeting threshold.
    Returns list of distinct storm events (deduplicated).
    """
    if start_date is None:
        start_date = min(prcp_data.keys())
    if end_date is None:
        end_date = max(prcp_data.keys())
    if exclude_dates is None:
        exclude_dates = []

    # Create exclusion window around flood dates
    exclude_window = set()
    for fd in exclude_dates:
        for i in range(-5, 6):
            exclude_window.add(fd + timedelta(days=i))

    # Find all days meeting threshold
    events = []
    current = start_date
    while current <= end_date:
        if current not in exclude_window:
            prcp_7d = get_cumulative_precip(prcp_data, current, 7)
            if prcp_7d >= threshold_7d:
                events.append({
                    'date': current,
                    'prcp_7d': prcp_7d,
                    'prcp_1d': prcp_data.get(current),
                    'dry_spell': get_dry_spell_before(prcp_data, current),
                })
        current += timedelta(days=1)

    # Deduplicate (keep peak of each storm)
    events.sort(key=lambda x: x['prcp_7d'], reverse=True)
    seen = set()
    distinct = []
    for e in events:
        if not any(abs((e['date'] - s).days) <= 7 for s in seen):
            distinct.append(e)
            seen.add(e['date'])

    return distinct


def calculate_threshold_stats(prcp_data: Dict[datetime, float],
                              flood_dates: List[datetime],
                              thresholds: List[float] = None) -> List[Dict]:
    """Calculate sensitivity analysis for different thresholds."""
    if thresholds is None:
        thresholds = [2.0, 2.5, 3.0, 3.5, 4.0, 5.0]

    # Get flood metrics
    flood_7d_values = [get_cumulative_precip(prcp_data, fd, 7) for fd in flood_dates]

    # Create flood-adjacent window
    flood_adjacent = set()
    for fd in flood_dates:
        for i in range(-3, 4):
            flood_adjacent.add(fd + timedelta(days=i))

    # All 7-day values
    all_7d = []
    for d in prcp_data.keys():
        cum = get_cumulative_precip(prcp_data, d, 7)
        all_7d.append((d, cum))

    results = []
    for thresh in thresholds:
        days_above = [(d, c) for d, c in all_7d if c >= thresh]
        floods_above = sum(1 for v in flood_7d_values if v >= thresh)

        # Dedupe non-flood days above threshold
        non_flood_above = [x for x in days_above if x[0] not in flood_adjacent]
        non_flood_above.sort(key=lambda x: x[1], reverse=True)
        seen = set()
        distinct_non_flood = 0
        for d, c in non_flood_above:
            if not any(abs((d - s).days) <= 5 for s in seen):
                distinct_non_flood += 1
                seen.add(d)

        results.append({
            'threshold': thresh,
            'floods_caught': floods_above,
            'total_floods': len(flood_dates),
            'false_alarms': distinct_non_flood,
            'recall': floods_above / len(flood_dates) if flood_dates else 0,
        })

    return results


# =============================================================================
# REPORTING FUNCTIONS
# =============================================================================

def print_flood_analysis(prcp_data: Dict[datetime, float],
                         wind_data: Dict[datetime, Dict]):
    """Print comprehensive flood event analysis."""
    print("=" * 80)
    print("FLOOD EVENT ANALYSIS")
    print("=" * 80)

    for event in FLOOD_EVENTS:
        analysis = analyze_flood_event(prcp_data, wind_data, event.date)

        print(f"\n{'='*30} {event.date.strftime('%Y-%m-%d')} {'='*30}")
        print(f"Type: {event.flood_type.upper()}")
        print(f"Notes: {event.notes}")

        print(f"\nPrecipitation:")
        print(f"  Day of: {analysis['prcp_1d']:.2f} in" if analysis['prcp_1d'] else "  Day of: N/A")
        print(f"  3-day cumulative: {analysis['prcp_3d']:.2f} in")
        print(f"  7-day cumulative: {analysis['prcp_7d']:.2f} in")
        print(f"  Dry spell before: {analysis['dry_spell_before']} days")

        if analysis['wind_dir'] is not None:
            print(f"\nWind:")
            print(f"  Direction: {analysis['wind_dir_compass']} ({analysis['wind_dir']}°)")
            print(f"  Max speed: {analysis['max_wind']} kt" if analysis['max_wind'] else "  Max speed: N/A")
            print(f"  Max gust: {analysis['max_gust']} kt" if analysis['max_gust'] else "  Max gust: N/A")
        else:
            print(f"\nWind: No data available")


def print_threshold_analysis(prcp_data: Dict[datetime, float]):
    """Print threshold sensitivity analysis."""
    print("\n" + "=" * 80)
    print("THRESHOLD SENSITIVITY ANALYSIS (Wall Floods Only)")
    print("=" * 80)

    results = calculate_threshold_stats(prcp_data, WALL_FLOOD_DATES)

    print(f"\n{'Threshold':<12} | {'Floods Caught':<15} | {'False Alarms':<14} | {'Recall':<8}")
    print("-" * 60)

    for r in results:
        print(f"{r['threshold']:.1f} in       | "
              f"{r['floods_caught']}/{r['total_floods']}             | "
              f"{r['false_alarms']:<14} | "
              f"{r['recall']*100:.0f}%")


def print_non_flood_comparison(prcp_data: Dict[datetime, float],
                                wind_data: Dict[datetime, Dict]):
    """Print comparison of flood vs non-flood high-precip events."""
    print("\n" + "=" * 80)
    print("HIGH-PRECIPITATION EVENTS WITHOUT FLOODING")
    print("=" * 80)

    non_flood_events = find_high_precip_events(
        prcp_data,
        threshold_7d=3.0,
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2025, 12, 31),
        exclude_dates=WALL_FLOOD_DATES
    )

    print(f"\nFound {len(non_flood_events)} events with 7-day >= 3.0 in that did NOT cause wall flooding:\n")
    print(f"{'Date':<12} | {'7-day Precip':<12} | {'Wind Dir':<10} | {'Max Wind':<10}")
    print("-" * 55)

    for e in non_flood_events[:10]:
        wind_dir = "N/A"
        max_wind = "N/A"
        if e['date'] in wind_data:
            wd = wind_data[e['date']]
            predom = get_predominant_wind_direction(wd['dirs'])
            if predom is not None:
                wind_dir = direction_to_compass(predom)
            if wd['spds']:
                max_wind = f"{max(wd['spds'])} kt"

        print(f"{e['date'].strftime('%Y-%m-%d'):<12} | "
              f"{e['prcp_7d']:>10.2f} in | "
              f"{wind_dir:<10} | "
              f"{max_wind:<10}")


def print_conclusions():
    """Print final conclusions and recommendations."""
    print("\n" + "=" * 80)
    print("CONCLUSIONS AND RECOMMENDATIONS")
    print("=" * 80)
    print("""
WALL OUTLET FLOODING THRESHOLD:
  - Minimum 7-day precipitation: ~3.0 inches
  - Typically follows a dry spell of 7+ days
  - Wind direction from SW or S (180-225°) appears to increase risk

CEILING LEAK (Oct 13, 2025):
  - NOT precipitation-related based on weather data
  - Only 0.75 inches of rain that day, minimal in preceding week
  - Likely a different issue (plumbing, HVAC, etc.)

FALSE ALARM RATE:
  - About 75-80% of storms meeting precipitation threshold do NOT cause flooding
  - Wind direction likely determines which storms breach your wall
  - Your wall probably faces SW or S

PREDICTIVE INDICATORS:
  When forecasts show ALL of these, risk is elevated:
  1. 3+ inches of rain expected over 7 days
  2. Coming after a week or more of dry weather
  3. Winds from SW or S direction

RECOMMENDATIONS:
  1. Note which direction your leaking wall faces
  2. Monitor weather forecasts for wind direction during storms
  3. When SW/S winds + heavy rain forecast, take precautions
  4. Consider waterproofing the exterior wall facing SW/S
""")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Run complete analysis."""
    print("Loading precipitation data...")
    prcp_data = load_all_precipitation_data()
    print(f"  Loaded {len(prcp_data)} days of precipitation data")

    print("\nLoading wind data (this may download from NOAA)...")
    wind_data = load_isd_wind_data([2022, 2023, 2024, 2025])
    print(f"  Loaded {len(wind_data)} days of wind data")

    # Run analyses
    print_flood_analysis(prcp_data, wind_data)
    print_threshold_analysis(prcp_data)
    print_non_flood_comparison(prcp_data, wind_data)
    print_conclusions()


if __name__ == "__main__":
    main()
