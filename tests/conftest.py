import pathlib
import pytest
import pandas as pd
import numpy as np

@pytest.fixture
def sample_csv_path():
    root = pathlib.Path(__file__).parents[1]
    p = root / "data" / "sample_diabetes_mellitus_data.csv"
    if not p.exists():
        pytest.skip(f"Sample CSV not found at {p}")
    return p

@pytest.fixture
def simple_df():
    return pd.DataFrame(
        {
            "a": [1.0, np.nan, 3.0],
            "b": ["x", "y", None],
            "c": [True, False, True],
        }
    )

@pytest.fixture
def categorical_df():
    return pd.DataFrame({"cat": ["red", "blue", "red"], "num": [1, 2, 3]})