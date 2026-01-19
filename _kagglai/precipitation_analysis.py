"""
Precipitation Analysis Module for Home Water Intrusion Investigation
=====================================================================

This module analyzes precipitation data to determine rainfall thresholds
that correlate with water intrusion events in a home.
"""

import csv
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import math


@dataclass
class PrecipitationRecord:
    """Single day precipitation record."""
    date: datetime
    prcp: Optional[float]  # Precipitation in inches, None if missing
    tmax: Optional[float] = None
    tmin: Optional[float] = None
    tavg: Optional[float] = None


@dataclass
class FloodEvent:
    """Recorded flood/water intrusion event."""
    date: datetime
    notes: str = ""


@dataclass
class DailyMetrics:
    """Computed metrics for a single day."""
    date: datetime
    prcp_1d: Optional[float]
    prcp_3d: Optional[float]
    prcp_7d: Optional[float]
    max_1d_in_7d: float  # Max single-day precip in trailing 7 days


class PrecipitationDataset:
    """Handles loading and querying precipitation data."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data: Dict[datetime, PrecipitationRecord] = {}
        self.station_name = ""
        self._load_data()

    def _load_data(self):
        """Load CSV data into memory."""
        with open(self.filepath, 'r') as f:
            reader = csv.reader(f)

            # First line is station name
            first_line = next(reader)
            self.station_name = first_line[0] if first_line else "Unknown"

            # Second line is headers
            headers = next(reader)

            for row in reader:
                if len(row) < 5:
                    continue

                try:
                    date = datetime.strptime(row[0], '%Y-%m-%d')

                    # Parse precipitation (column index 4)
                    prcp_str = row[4].strip() if len(row) > 4 else ""
                    prcp = float(prcp_str) if prcp_str else None

                    # Parse temperatures if available
                    tavg = float(row[1]) if len(row) > 1 and row[1].strip() else None
                    tmax = float(row[2]) if len(row) > 2 and row[2].strip() else None
                    tmin = float(row[3]) if len(row) > 3 and row[3].strip() else None

                    self.data[date] = PrecipitationRecord(
                        date=date, prcp=prcp, tmax=tmax, tmin=tmin, tavg=tavg
                    )
                except (ValueError, IndexError):
                    continue

    @property
    def date_range(self) -> Tuple[datetime, datetime]:
        """Return (min_date, max_date) of dataset."""
        dates = sorted(self.data.keys())
        return (dates[0], dates[-1]) if dates else (None, None)

    @property
    def coverage_stats(self) -> Dict:
        """Return data coverage statistics."""
        total = len(self.data)
        with_prcp = sum(1 for r in self.data.values() if r.prcp is not None)
        return {
            "total_days": total,
            "days_with_prcp": with_prcp,
            "days_missing_prcp": total - with_prcp,
            "coverage_pct": (with_prcp / total * 100) if total > 0 else 0
        }

    def get_prcp(self, date: datetime) -> Optional[float]:
        """Get precipitation for a specific date."""
        record = self.data.get(date)
        return record.prcp if record else None

    def get_cumulative(self, end_date: datetime, days: int) -> Optional[float]:
        """
        Get cumulative precipitation for N days ending on end_date.
        Returns None only if ALL days are missing data.
        """
        total = 0.0
        has_any_data = False

        for i in range(days):
            d = end_date - timedelta(days=i)
            prcp = self.get_prcp(d)
            if prcp is not None:
                total += prcp
                has_any_data = True

        return total if has_any_data else None

    def get_max_single_day(self, end_date: datetime, days: int) -> float:
        """Get maximum single-day precipitation in N-day window."""
        max_val = 0.0
        for i in range(days):
            d = end_date - timedelta(days=i)
            prcp = self.get_prcp(d)
            if prcp is not None and prcp > max_val:
                max_val = prcp
        return max_val

    def get_window(self, center_date: datetime, days_before: int = 7,
                   days_after: int = 3) -> List[PrecipitationRecord]:
        """Get precipitation records around a date."""
        records = []
        for i in range(-days_before, days_after + 1):
            d = center_date + timedelta(days=i)
            if d in self.data:
                records.append(self.data[d])
        return records


class FloodAnalyzer:
    """Analyzes relationship between precipitation and flood events."""

    def __init__(self, datasets: List[PrecipitationDataset],
                 flood_events: List[FloodEvent]):
        self.datasets = datasets
        self.flood_events = flood_events
        self.flood_dates = {e.date for e in flood_events}

        # Mark dates near floods as "adjacent" (within 5 days)
        self.flood_adjacent = set()
        for fd in self.flood_dates:
            for i in range(-5, 6):
                self.flood_adjacent.add(fd + timedelta(days=i))

    def get_best_prcp(self, date: datetime) -> Optional[float]:
        """Get precipitation from first dataset that has data for date."""
        for ds in self.datasets:
            prcp = ds.get_prcp(date)
            if prcp is not None:
                return prcp
        return None

    def get_best_cumulative(self, date: datetime, days: int) -> Optional[float]:
        """Get cumulative precipitation, preferring most complete dataset."""
        best_total = None
        best_count = 0

        for ds in self.datasets:
            total = 0.0
            count = 0
            for i in range(days):
                d = date - timedelta(days=i)
                prcp = ds.get_prcp(d)
                if prcp is not None:
                    total += prcp
                    count += 1

            if count > best_count:
                best_count = count
                best_total = total

        return best_total if best_count > 0 else None

    def compute_daily_metrics(self, start_date: datetime,
                               end_date: datetime) -> List[DailyMetrics]:
        """Compute metrics for all dates in range."""
        metrics = []
        current = start_date

        while current <= end_date:
            prcp_1d = self.get_best_prcp(current)
            prcp_3d = self.get_best_cumulative(current, 3)
            prcp_7d = self.get_best_cumulative(current, 7)

            # Max single day in 7-day window
            max_1d = 0.0
            for i in range(7):
                d = current - timedelta(days=i)
                p = self.get_best_prcp(d)
                if p is not None and p > max_1d:
                    max_1d = p

            metrics.append(DailyMetrics(
                date=current,
                prcp_1d=prcp_1d,
                prcp_3d=prcp_3d,
                prcp_7d=prcp_7d,
                max_1d_in_7d=max_1d
            ))

            current += timedelta(days=1)

        return metrics

    def analyze_flood_events(self) -> Dict:
        """Analyze precipitation around each flood event."""
        results = []

        for event in self.flood_events:
            # Get window of data
            window_data = []
            for i in range(-7, 4):
                d = event.date + timedelta(days=i)
                prcp = self.get_best_prcp(d)
                cum_3d = self.get_best_cumulative(d, 3)
                cum_7d = self.get_best_cumulative(d, 7)
                window_data.append({
                    "date": d,
                    "offset": i,
                    "prcp": prcp,
                    "cum_3d": cum_3d,
                    "cum_7d": cum_7d,
                    "is_flood_day": i == 0
                })

            # Metrics for flood day itself
            flood_day_prcp = self.get_best_prcp(event.date)
            flood_day_3d = self.get_best_cumulative(event.date, 3)
            flood_day_7d = self.get_best_cumulative(event.date, 7)

            results.append({
                "event": event,
                "window": window_data,
                "metrics": {
                    "prcp_1d": flood_day_prcp,
                    "prcp_3d": flood_day_3d,
                    "prcp_7d": flood_day_7d
                }
            })

        return {"flood_events": results}

    def find_high_precip_non_flood_events(self, threshold_7d: float = 2.0,
                                          start_date: datetime = None,
                                          end_date: datetime = None) -> List[Dict]:
        """
        Find high-precipitation periods that did NOT cause recorded flooding.
        These are either false alarms or potentially unrecorded flood events.
        """
        if start_date is None:
            start_date = min(ds.date_range[0] for ds in self.datasets)
        if end_date is None:
            end_date = max(ds.date_range[1] for ds in self.datasets)

        metrics = self.compute_daily_metrics(start_date, end_date)

        # Filter to high-precip days not adjacent to floods
        high_precip = [
            m for m in metrics
            if m.prcp_7d is not None
            and m.prcp_7d >= threshold_7d
            and m.date not in self.flood_adjacent
        ]

        # Deduplicate (keep peak day for each storm event)
        high_precip.sort(key=lambda x: x.prcp_7d, reverse=True)
        seen_windows = set()
        distinct_events = []

        for m in high_precip:
            is_duplicate = any(abs((m.date - s).days) <= 7 for s in seen_windows)
            if not is_duplicate:
                distinct_events.append({
                    "date": m.date,
                    "prcp_1d": m.prcp_1d,
                    "prcp_3d": m.prcp_3d,
                    "prcp_7d": m.prcp_7d,
                    "max_1d_in_7d": m.max_1d_in_7d
                })
                seen_windows.add(m.date)

        return distinct_events

    def compute_statistics(self, start_date: datetime,
                          end_date: datetime) -> Dict:
        """Compute statistical summary of precipitation data."""
        metrics = self.compute_daily_metrics(start_date, end_date)

        # Extract 7-day values (excluding None)
        values_7d = [m.prcp_7d for m in metrics if m.prcp_7d is not None]
        values_1d = [m.prcp_1d for m in metrics if m.prcp_1d is not None]

        def calc_stats(values: List[float]) -> Dict:
            if not values:
                return {}
            n = len(values)
            mean = sum(values) / n
            variance = sum((x - mean)**2 for x in values) / n
            std = math.sqrt(variance)
            sorted_vals = sorted(values)

            percentiles = {}
            for p in [50, 75, 90, 95, 99]:
                idx = int(n * p / 100)
                percentiles[p] = sorted_vals[min(idx, n-1)]

            return {
                "n": n,
                "mean": mean,
                "std": std,
                "min": min(values),
                "max": max(values),
                "percentiles": percentiles
            }

        return {
            "period": {"start": start_date, "end": end_date},
            "prcp_1d_stats": calc_stats(values_1d),
            "prcp_7d_stats": calc_stats(values_7d)
        }

    def threshold_analysis(self, start_date: datetime, end_date: datetime,
                          thresholds: List[float] = None) -> List[Dict]:
        """
        Analyze how different thresholds perform at separating
        flood from non-flood events.
        """
        if thresholds is None:
            thresholds = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

        metrics = self.compute_daily_metrics(start_date, end_date)

        # Get flood event metrics (7-day cumulative on flood days)
        flood_7d_values = []
        for event in self.flood_events:
            if start_date <= event.date <= end_date:
                cum_7d = self.get_best_cumulative(event.date, 7)
                if cum_7d is not None:
                    flood_7d_values.append(cum_7d)

        # All 7-day values
        all_7d = [m.prcp_7d for m in metrics if m.prcp_7d is not None]

        results = []
        for thresh in thresholds:
            days_above = sum(1 for v in all_7d if v >= thresh)
            floods_above = sum(1 for v in flood_7d_values if v >= thresh)
            floods_below = len(flood_7d_values) - floods_above
            non_flood_above = days_above - floods_above

            # Precision and recall (if floods_above > 0)
            precision = floods_above / days_above if days_above > 0 else 0
            recall = floods_above / len(flood_7d_values) if flood_7d_values else 0

            results.append({
                "threshold_inches": thresh,
                "days_above": days_above,
                "floods_captured": floods_above,
                "floods_missed": floods_below,
                "false_alarms": non_flood_above,
                "precision": precision,
                "recall": recall
            })

        return results


def print_flood_analysis(analyzer: FloodAnalyzer):
    """Print formatted analysis of flood events."""
    analysis = analyzer.analyze_flood_events()

    print("=" * 70)
    print("FLOOD EVENT PRECIPITATION ANALYSIS")
    print("=" * 70)

    for item in analysis["flood_events"]:
        event = item["event"]
        metrics = item["metrics"]
        window = item["window"]

        print(f"\n{'='*20} {event.date.strftime('%Y-%m-%d')} {'='*20}")
        if event.notes:
            print(f"Notes: {event.notes}")

        print("\nDate           PRCP    3-day    7-day")
        print("-" * 45)
        for w in window:
            prcp_s = f"{w['prcp']:.2f}" if w['prcp'] is not None else "MISS"
            cum3_s = f"{w['cum_3d']:.2f}" if w['cum_3d'] is not None else "N/A"
            cum7_s = f"{w['cum_7d']:.2f}" if w['cum_7d'] is not None else "N/A"
            marker = " <-- FLOOD" if w['is_flood_day'] else ""
            print(f"{w['date'].strftime('%Y-%m-%d')}   {prcp_s:>6}   {cum3_s:>6}   {cum7_s:>6}{marker}")

        print(f"\nFlood day metrics:")
        for key, val in metrics.items():
            val_s = f"{val:.2f}" if val is not None else "MISSING"
            print(f"  {key}: {val_s}")


def print_statistics(analyzer: FloodAnalyzer, start_date: datetime, end_date: datetime):
    """Print statistical summary."""
    stats = analyzer.compute_statistics(start_date, end_date)

    print("\n" + "=" * 70)
    print(f"PRECIPITATION STATISTICS ({start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')})")
    print("=" * 70)

    for metric_name, label in [("prcp_1d_stats", "Single-Day"), ("prcp_7d_stats", "7-Day Cumulative")]:
        s = stats[metric_name]
        if not s:
            continue
        print(f"\n{label} Precipitation:")
        print(f"  N observations: {s['n']}")
        print(f"  Mean: {s['mean']:.2f} inches")
        print(f"  Std Dev: {s['std']:.2f} inches")
        print(f"  Max: {s['max']:.2f} inches")
        print("  Percentiles:")
        for p, val in s['percentiles'].items():
            print(f"    {p}th: {val:.2f} inches")


def print_threshold_analysis(analyzer: FloodAnalyzer, start_date: datetime, end_date: datetime):
    """Print threshold sensitivity analysis."""
    results = analyzer.threshold_analysis(start_date, end_date)

    print("\n" + "=" * 70)
    print("THRESHOLD SENSITIVITY ANALYSIS (7-day cumulative)")
    print("=" * 70)
    print("\nThreshold | Days Above | Floods Captured | False Alarms | Recall")
    print("-" * 70)

    for r in results:
        print(f"  {r['threshold_inches']:.1f} in   |    {r['days_above']:4d}    |"
              f"      {r['floods_captured']}/{r['floods_captured']+r['floods_missed']}        |"
              f"     {r['false_alarms']:4d}    | {r['recall']*100:.0f}%")


def print_non_flood_high_precip(analyzer: FloodAnalyzer, threshold: float = 2.0,
                                 start_date: datetime = None, end_date: datetime = None):
    """Print high-precip events without recorded flooding."""
    events = analyzer.find_high_precip_non_flood_events(threshold, start_date, end_date)

    print("\n" + "=" * 70)
    print(f"HIGH-PRECIP EVENTS WITHOUT RECORDED FLOODING (7-day >= {threshold} in)")
    print("(Candidates for potentially unrecorded flood incidents)")
    print("=" * 70)

    print(f"\nFound {len(events)} distinct events:\n")
    print("Date         1-day    3-day    7-day   Max1d(7d)")
    print("-" * 55)

    for e in events[:15]:
        d1 = f"{e['prcp_1d']:.2f}" if e['prcp_1d'] is not None else "MISS"
        d3 = f"{e['prcp_3d']:.2f}" if e['prcp_3d'] is not None else "MISS"
        d7 = f"{e['prcp_7d']:.2f}" if e['prcp_7d'] is not None else "MISS"
        max1 = f"{e['max_1d_in_7d']:.2f}"
        print(f"{e['date'].strftime('%Y-%m-%d')}   {d1:>6}   {d3:>6}   {d7:>6}     {max1}")


# ============================================================================
# MAIN ANALYSIS FOR HOME WATER INTRUSION INVESTIGATION
# ============================================================================

if __name__ == "__main__":
    import os

    # File paths - all available weather stations
    DOWNLOADS = os.path.expanduser("~/Downloads")
    STATION_FILES = [
        os.path.join(DOWNLOADS, "USW00023272.csv"),      # Downtown SF - best coverage
        os.path.join(DOWNLOADS, "US1CASF0017.csv"),      # SF 1.6 SE - second best
        os.path.join(DOWNLOADS, "USC00047767.csv"),      # Oceanside SF
        os.path.join(DOWNLOADS, "precipitation_san_franisco_US1CASF0020.csv"),  # SF 3.1 W
    ]

    # Load datasets
    print("Loading precipitation data from all available stations...")
    datasets = []

    for filepath in STATION_FILES:
        if os.path.exists(filepath):
            ds = PrecipitationDataset(filepath)
            datasets.append(ds)
            stats = ds.coverage_stats
            print(f"  Loaded: {ds.station_name}")
            print(f"    Date range: {ds.date_range[0].strftime('%Y-%m-%d')} to {ds.date_range[1].strftime('%Y-%m-%d')}")
            print(f"    Coverage: {stats['days_with_prcp']}/{stats['total_days']} days ({stats['coverage_pct']:.1f}%)")

    # Define flood events
    flood_events = [
        FloodEvent(datetime(2022, 12, 31), "Water from outlets in wall"),
        FloodEvent(datetime(2025, 10, 13), "Water from outlets in wall"),
        FloodEvent(datetime(2025, 12, 24), "Water from outlets in wall"),
        FloodEvent(datetime(2025, 12, 26), "Water from outlets in wall"),
    ]

    # Create analyzer
    analyzer = FloodAnalyzer(datasets, flood_events)

    # Analysis period
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2025, 12, 31)

    # Run all analyses
    print_flood_analysis(analyzer)
    print_statistics(analyzer, start_date, end_date)
    print_threshold_analysis(analyzer, start_date, end_date)
    print_non_flood_high_precip(analyzer, threshold=2.0, start_date=start_date, end_date=end_date)

    # Final summary
    print("\n" + "=" * 70)
    print("CONCLUSIONS")
    print("=" * 70)
    print("""
Based on analysis combining both SF weather stations:

1. CONFIRMED FLOOD-CORRELATED EVENTS:
   - Dec 31, 2022: Extremely heavy rain (2.51+ inches single day)
   - Dec 24-26, 2025: Sustained multi-day rain event (~1.4 in peak, 2-3 in cumulative)

2. ANOMALOUS EVENT:
   - Oct 13, 2025: Even with downtown data, minimal precipitation recorded.
     This event likely has a NON-PRECIPITATION cause.

3. POTENTIAL THRESHOLD:
   Conservative: 7-day cumulative >= 2.0 inches with peak day >= 1.3 inches

4. UNEXPLAINED NON-FLOODS:
   Several events with HIGHER precipitation did not cause flooding.
   Possible explanations: wind direction, hourly intensity, building factors,
   or unrecorded flood incidents.
""")
