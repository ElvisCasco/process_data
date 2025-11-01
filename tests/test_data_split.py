import pytest
import pandas as pd
from process_data import data_split


def test_data_split_basic(tmp_path):
    """Test basic train/test split"""
    csv_file = tmp_path / "test_data.csv"
    df = pd.DataFrame({
        "age": range(100),
        "diabetes_mellitus": [0, 1] * 50
    })
    df.to_csv(csv_file, index=False)
    
    train_df, test_df = data_split(csv_file, test_size=0.3, random_state=42)
    
    assert isinstance(train_df, pd.DataFrame)
    assert isinstance(test_df, pd.DataFrame)
    assert len(train_df) == 70
    assert len(test_df) == 30
    assert len(train_df) + len(test_df) == 100


def test_data_split_random_state(tmp_path):
    """Test reproducibility with random_state"""
    csv_file = tmp_path / "test_data.csv"
    df = pd.DataFrame({"age": range(50), "target": [0, 1] * 25})
    df.to_csv(csv_file, index=False)
    
    train1, test1 = data_split(csv_file, test_size=0.2, random_state=42)
    train2, test2 = data_split(csv_file, test_size=0.2, random_state=42)
    
    pd.testing.assert_frame_equal(train1, train2)
    pd.testing.assert_frame_equal(test1, test2)


def test_data_split_different_ratios(tmp_path):
    """Test different train/test ratios"""
    csv_file = tmp_path / "test_data.csv"
    df = pd.DataFrame({"col1": range(100)})
    df.to_csv(csv_file, index=False)
    
    # Test 80/20 split
    train_df, test_df = data_split(csv_file, test_size=0.2, random_state=42)
    assert len(train_df) == 80
    assert len(test_df) == 20
    
    # Test 70/30 split
    train_df, test_df = data_split(csv_file, test_size=0.3, random_state=42)
    assert len(train_df) == 70
    assert len(test_df) == 30