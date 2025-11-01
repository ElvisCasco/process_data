import pytest
import pandas as pd
import numpy as np
from process_data import data_remove_nans


def test_data_remove_nans_specific_columns():
    """Test removing NaNs from specific columns"""
    df = pd.DataFrame({
        "age": [25, np.nan, 35, 40],
        "gender": ["M", "F", None, "M"],
        "ethnicity": ["A", "B", "C", None],
        "height": [170, 175, np.nan, 180]
    })
    
    result = data_remove_nans(df, columns=["age", "gender", "ethnicity"])
    
    assert len(result) == 2  # Only 2 rows have no NaNs in specified columns
    assert result["age"].isna().sum() == 0
    assert result["gender"].isna().sum() == 0
    assert result["ethnicity"].isna().sum() == 0


def test_data_remove_nans_all_columns():
    """Test removing NaNs from all columns when columns=None"""
    df = pd.DataFrame({
        "col1": [1, 2, np.nan, 4],
        "col2": [5, np.nan, 7, 8],
        "col3": [9, 10, 11, 12]
    })
    
    result = data_remove_nans(df, columns=None)
    
    assert len(result) == 2  # Only rows 0 and 3 have no NaNs
    assert result.isna().sum().sum() == 0


def test_data_remove_nans_no_nans():
    """Test with DataFrame that has no NaNs"""
    df = pd.DataFrame({
        "age": [25, 30, 35],
        "gender": ["M", "F", "M"]
    })
    
    result = data_remove_nans(df, columns=["age", "gender"])
    
    assert len(result) == len(df)
    pd.testing.assert_frame_equal(result, df)


def test_data_remove_nans_preserves_other_columns():
    """Test that other columns are preserved"""
    df = pd.DataFrame({
        "age": [25, np.nan, 35],
        "gender": ["M", "F", "M"],
        "height": [170, 175, np.nan],
        "id": [1, 2, 3]
    })
    
    result = data_remove_nans(df, columns=["age", "gender"])
    
    assert "height" in result.columns
    assert "id" in result.columns
    assert len(result) == 2