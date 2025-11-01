import pytest
import pandas as pd
from process_data import data_encoding


def test_data_encoding_single_column():
    """Test one-hot encoding of a single column"""
    df = pd.DataFrame({
        "ethnicity": ["A", "B", "C", "A", "B"],
        "age": [25, 30, 35, 40, 45]
    })
    
    result = data_encoding(df, columns=["ethnicity"])
    
    # Check that ethnicity dummies are created
    assert "ethnicity_A" in result.columns
    assert "ethnicity_B" in result.columns
    assert "ethnicity_C" in result.columns
    
    # Check values
    assert result["ethnicity_A"].iloc[0] == 1
    assert result["ethnicity_B"].iloc[1] == 1
    assert result["ethnicity_C"].iloc[2] == 1
    
    # Check age is preserved
    assert "age" in result.columns


def test_data_encoding_multiple_columns():
    """Test encoding multiple columns"""
    df = pd.DataFrame({
        "ethnicity": ["A", "B", "A"],
        "category": ["X", "Y", "X"],
        "value": [1, 2, 3]
    })
    
    result = data_encoding(df, columns=["ethnicity", "category"])
    
    assert "ethnicity_A" in result.columns
    assert "ethnicity_B" in result.columns
    assert "category_X" in result.columns
    assert "category_Y" in result.columns
    assert "value" in result.columns


def test_data_encoding_drops_original():
    """Test that original columns are dropped"""
    df = pd.DataFrame({
        "ethnicity": ["A", "B", "C"],
        "age": [25, 30, 35]
    })
    
    result = data_encoding(df, columns=["ethnicity"])
    
    # Original ethnicity column should be dropped
    assert "ethnicity" not in result.columns
    # But encoded columns should exist
    assert "ethnicity_A" in result.columns


def test_data_encoding_with_nans():
    """Test encoding with NaN values"""
    df = pd.DataFrame({
        "ethnicity": ["A", None, "B", "A"],
        "age": [25, 30, 35, 40]
    })
    
    result = data_encoding(df, columns=["ethnicity"])
    
    # Check that encoding works despite NaN
    assert "ethnicity_A" in result.columns
    assert "ethnicity_B" in result.columns