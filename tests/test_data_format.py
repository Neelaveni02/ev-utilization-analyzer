import pandas as pd
from pathlib import Path
import pytest

from src.io_utils import load_acn_csv
from src.exceptions import DataFormatError, DataSourceError

def test_missing_file_raises_error():
    with pytest.raises(DataSourceError):
        load_acn_csv(Path("data/raw/does_not_exist.csv"))

def test_missing_columns_raises_error(tmp_path):
    bad_csv = tmp_path / "bad.csv"
    pd.DataFrame({"A": [1], "B": [2]}).to_csv(bad_csv, index=False)

    with pytest.raises(DataFormatError):
        load_acn_csv(bad_csv)
