import pytest
import pandas as pd
import numpy as np
from pathlib import Path


@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for testing"""
    return pd.DataFrame({
        "age": [25, 30, 35, 40, 45],
        "height": [170, 175, 180, 165, 172],
        "weight": [70, 80, 75, 65, 73],
        "gender": ["M", "F", "M", "F", "M"],
        "diabetes_mellitus": [0, 1, 0, 1, 0]
    })


@pytest.fixture
def sample_csv(tmp_path):
    """Create a temporary CSV file for testing"""
    csv_file = tmp_path / "test_data.csv"
    df = pd.DataFrame({
        "age": range(100),
        "gender": ["M", "F"] * 50,
        "diabetes_mellitus": [0, 1] * 50
    })
    df.to_csv(csv_file, index=False)
    return csv_file


@pytest.fixture
def sample_data_with_nans():
    """Create DataFrame with NaN values"""
    return pd.DataFrame({
        "age": [25, np.nan, 35, 40],
        "gender": ["M", "F", None, "M"],
        "ethnicity": ["A", "B", "C", None],
        "height": [170, 175, np.nan, 180],
        "weight": [70, np.nan, 85, 75]
    })