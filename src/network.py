"""
Charging network model (composition of Station objects).
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List

from src.station import Station

@dataclass
class ChargingNetwork:
    """
    Represents a network of charging stations.
    """
    name: str = "Caltech ACN"
    stations: Dict[str, Station] = field(default_factory=dict)

    def get_or_create_station(self, station_id: str) -> Station:
        if station_id not in self.stations:
            self.stations[station_id] = Station(station_id=station_id)
        return self.stations[station_id]

    def add_session(self, station_id: str, start: datetime, end: datetime) -> None:
        station = self.get_or_create_station(station_id)
        station.add_session(start, end)

    def recommend_actions(
        self,
        window_start: datetime,
        window_end: datetime,
        overuse_threshold: float = 0.7,
        underuse_threshold: float = 0.15
    ) -> List[str]:

        recommendations = []
        for station_id, station in self.stations.items():
            utilization = station.compute_utilization(window_start, window_end)

            if utilization >= overuse_threshold:
                recommendations.append(
                    f"Station {station_id} is overused ({utilization:.2f}). Consider adding chargers."
                )
            elif utilization <= underuse_threshold:
                recommendations.append(
                    f"Station {station_id} is underused ({utilization:.2f}). Consider maintenance or incentives."
                )

        return recommendations
