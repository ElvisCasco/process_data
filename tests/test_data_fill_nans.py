import pytest
import pandas as pd
import numpy as np
from process_data import data_fill_nans


def test_data_fill_nans_with_mean():
    """Test filling NaNs with mean values"""
    df = pd.DataFrame({
        "height": [170.0, 180.0, np.nan, 175.0],
        "weight": [70.0, np.nan, 85.0, 75.0]
    })
    
    result = data_fill_nans(df, columns=["height", "weight"])
    
    # Check no NaNs remain
    assert result["height"].isna().sum() == 0
    assert result["weight"].isna().sum() == 0
    
    # Check mean values are correct
    expected_height_mean = (170.0 + 180.0 + 175.0) / 3
    expected_weight_mean = (70.0 + 85.0 + 75.0) / 3
    
    assert result["height"].iloc[2] == pytest.approx(expected_height_mean)
    assert result["weight"].iloc[1] == pytest.approx(expected_weight_mean)


def test_data_fill_nans_no_nans():
    """Test with DataFrame that has no NaNs"""
    df = pd.DataFrame({
        "height": [170.0, 180.0, 175.0],
        "weight": [70.0, 80.0, 75.0]
    })
    
    result = data_fill_nans(df, columns=["height", "weight"])
    
    pd.testing.assert_frame_equal(result, df)


def test_data_fill_nans_single_column():
    """Test filling NaNs in a single column"""
    df = pd.DataFrame({
        "height": [170.0, np.nan, 180.0],
        "weight": [70.0, 80.0, 75.0]
    })
    
    result = data_fill_nans(df, columns=["height"])
    
    assert result["height"].isna().sum() == 0
    assert result["height"].iloc[1] == 175.0  # Mean of 170 and 180


def test_data_fill_nans_preserves_other_columns():
    """Test that columns not specified are not modified"""
    df = pd.DataFrame({
        "height": [170.0, np.nan, 180.0],
        "weight": [70.0, np.nan, 75.0],
        "age": [25, 30, np.nan]
    })
    
    result = data_fill_nans(df, columns=["height", "weight"])
    
    assert result["height"].isna().sum() == 0
    assert result["weight"].isna().sum() == 0
    assert result["age"].isna().sum() == 1  # age should still have NaN