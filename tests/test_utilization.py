from datetime import datetime
import pandas as pd

from src.analysis import compute_utilization_by_station

def test_utilization_simple_case():
    """
    One station connected for 30 minutes in a 1-hour window
    => utilization should be 0.5
    """
    df = pd.DataFrame({
        "stationID": ["S1"],
        "connectionTime": ["2024-01-01 10:00:00"],
        "disconnectTime": ["2024-01-01 10:30:00"],
        "kWhDelivered": [4.0]
    })

    window_start = datetime.fromisoformat("2024-01-01 10:00:00")
    window_end = datetime.fromisoformat("2024-01-01 11:00:00")

    result = compute_utilization_by_station(df, (window_start, window_end))
    utilization = float(result.loc[0, "utilization"])

    assert abs(utilization - 0.5) < 1e-6
