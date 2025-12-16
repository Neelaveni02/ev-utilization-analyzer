"""
Analysis utilities for utilization calculations.
"""

from datetime import datetime
from typing import Tuple
import pandas as pd

def compute_utilization_by_station(
    df: pd.DataFrame,
    window: Tuple[datetime, datetime]
) -> pd.DataFrame:

    window_start, window_end = window
    total_seconds = (window_end - window_start).total_seconds()

    df = df.copy()
    df["connectionTime"] = pd.to_datetime(df["connectionTime"], errors="coerce")
    df["disconnectTime"] = pd.to_datetime(df["disconnectTime"], errors="coerce")

    df = df.dropna(subset=["connectionTime", "disconnectTime"])
    df = df[df["disconnectTime"] > df["connectionTime"]]

    df["overlap_start"] = df["connectionTime"].clip(lower=window_start)
    df["overlap_end"] = df["disconnectTime"].clip(upper=window_end)
    df["overlap_sec"] = (df["overlap_end"] - df["overlap_start"]).dt.total_seconds().clip(lower=0)

    summary = df.groupby("stationID").agg(
        utilization_seconds=("overlap_sec", "sum"),
        session_count=("stationID", "count")
    ).reset_index()

    summary["utilization"] = summary["utilization_seconds"] / total_seconds
    return summary.sort_values("utilization", ascending=False)
