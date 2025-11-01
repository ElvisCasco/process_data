import pytest
import pandas as pd
import numpy as np
from process_data import data_binary


def test_data_binary_m_f():
    """Test binary encoding with M/F values"""
    df = pd.DataFrame({
        "gender": ["M", "F", "M", "F"],
        "age": [25, 30, 35, 40]
    })
    
    result = data_binary(df, column="gender")
    
    # Check binary values (M=1, F=0 or vice versa)
    assert result["gender"].dtype in [np.int64, np.int32, np.float64]
    assert set(result["gender"].unique()) == {0, 1}


def test_data_binary_male_female():
    """Test binary encoding with Male/Female values"""
    df = pd.DataFrame({
        "gender": ["Male", "Female", "Male", "Female"],
        "age": [25, 30, 35, 40]
    })
    
    result = data_binary(df, column="gender")
    
    assert result["gender"].dtype in [np.int64, np.int32, np.float64]
    assert set(result["gender"].unique()) == {0, 1}


def test_data_binary_mixed_formats():
    """Test binary encoding with mixed M/F and Male/Female"""
    df = pd.DataFrame({
        "gender": ["M", "Female", "Male", "F"],
        "age": [25, 30, 35, 40]
    })
    
    result = data_binary(df, column="gender")
    
    assert result["gender"].dtype in [np.int64, np.int32, np.float64]
    assert set(result["gender"].unique()) == {0, 1}
    # M and Male should map to same value
    # F and Female should map to same value


def test_data_binary_with_nans():
    """Test binary encoding preserves NaN values"""
    df = pd.DataFrame({
        "gender": ["M", None, "F", "M"],
        "age": [25, 30, 35, 40]
    })
    
    result = data_binary(df, column="gender")
    
    # NaN should be preserved
    assert result["gender"].isna().sum() == 1


def test_data_binary_preserves_other_columns():
    """Test that other columns are not modified"""
    df = pd.DataFrame({
        "gender": ["M", "F", "M"],
        "age": [25, 30, 35],
        "height": [170, 165, 180]
    })
    
    result = data_binary(df, column="gender")
    
    assert "age" in result.columns
    assert "height" in result.columns
    pd.testing.assert_series_equal(result["age"], df["age"])
    pd.testing.assert_series_equal(result["height"], df["height"])