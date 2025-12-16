"""
Charging session model and generator.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Iterator, Any

@dataclass(frozen=True)
class ChargingSession:
    """
    Immutable charging session record.
    """
    station_id: str
    connection_time: datetime
    disconnect_time: datetime
    kwh_delivered: float

    @property
    def duration_hours(self) -> float:
        seconds = (self.disconnect_time - self.connection_time).total_seconds()
        return max(0.0, seconds / 3600.0)

def parse_datetime(value: Any) -> datetime:
    return datetime.fromisoformat(str(value).replace("Z", "").strip())

def session_generator(df_iter) -> Iterator[ChargingSession]:
    """
    Generator that yields ChargingSession objects (memory efficient).
    """
    for chunk in df_iter:
        for _, row in chunk.iterrows():
            yield ChargingSession(
                station_id=str(row["stationID"]),
                connection_time=parse_datetime(row["connectionTime"]),
                disconnect_time=parse_datetime(row["disconnectTime"]),
                kwh_delivered=float(row.get("kWhDelivered", 0.0) or 0.0),
            )
