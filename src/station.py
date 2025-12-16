"""
Station model: utilization, sorting, display.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Tuple, Dict

@dataclass
class Station:
    """
    Represents a charging station.

    Relationship: Station objects are contained inside ChargingNetwork (composition).

    Attributes:
        station_id: Unique station identifier.
        location: Optional location label (if available / inferred).
        network: Network name (e.g., Caltech ACN).
        sessions: List of session intervals stored as (start, end).
    """
    station_id: str
    location: str = "Unknown"
    network: str = "ACN"
    sessions: List[Tuple[datetime, datetime]] = field(default_factory=list)

    def add_session(self, start: datetime, end: datetime) -> None:
        """Add a session interval to this station."""
        if end > start:
            self.sessions.append((start, end))

    def compute_utilization(self, window_start: datetime, window_end: datetime) -> float:
        """
        Compute utilization fraction in [0,1] for a given time window.
        Utilization = (total overlapped connected time) / (window length).

        Note: This counts "occupied/connected time". (Good metric for congestion.)
        """
        total_window = (window_end - window_start).total_seconds()
        if total_window <= 0:
            return 0.0

        occupied = 0.0
        for s, e in self.sessions:  # required: for-loop iterating sessions
            overlap_start = max(s, window_start)
            overlap_end = min(e, window_end)
            if overlap_end > overlap_start:
                occupied += (overlap_end - overlap_start).total_seconds()

        return min(1.0, max(0.0, occupied / total_window))

    def __lt__(self, other: "Station") -> bool:
        """
        Operator overloading: sort by average utilization (descending if you reverse sort).
        We'll use a simple proxy: total session time.
        """
        return self.total_connected_seconds() < other.total_connected_seconds()

    def total_connected_seconds(self) -> float:
        """Total connected seconds across all sessions."""
        return sum((e - s).total_seconds() for s, e in self.sessions if e > s)

    def __str__(self) -> str:
        """Human-readable station summary."""
        hours = self.total_connected_seconds() / 3600.0
        return f"Station({self.station_id}, sessions={len(self.sessions)}, connected_hours={hours:.2f})"
