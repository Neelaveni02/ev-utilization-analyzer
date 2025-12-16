"""
Input/output utilities.
"""

from pathlib import Path
import json
import pandas as pd

from src.exceptions import DataSourceError, DataFormatError

REQUIRED_COLUMNS = ["stationID", "connectionTime", "disconnectTime"]

def load_acn_csv(path: Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise DataSourceError("CSV file not found.")
    except Exception as e:
        raise DataSourceError(str(e))

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise DataFormatError(f"Missing columns: {missing}")

    return df

def write_json(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
