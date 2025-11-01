import pytest
import pandas as pd
from pathlib import Path
from process_data import data_loader


def test_data_loader_with_csv(tmp_path):
    """Test loading a CSV file"""
    # Create a temporary CSV file
    csv_file = tmp_path / "test_data.csv"
    df = pd.DataFrame({
        "age": [25, 30, 35],
        "gender": ["M", "F", "M"],
        "diabetes_mellitus": [0, 1, 0]
    })
    df.to_csv(csv_file, index=False)
    
    # Load the CSV
    loaded_df = data_loader(csv_file)
    
    # Assertions
    assert isinstance(loaded_df, pd.DataFrame)
    assert loaded_df.shape == (3, 3)
    assert list(loaded_df.columns) == ["age", "gender", "diabetes_mellitus"]
    pd.testing.assert_frame_equal(loaded_df, df)


def test_data_loader_file_not_found():
    """Test error handling when file doesn't exist"""
    with pytest.raises(FileNotFoundError):
        data_loader("nonexistent_file.csv")


def test_data_loader_with_path_object(tmp_path):
    """Test loading with Path object"""
    csv_file = tmp_path / "test_data.csv"
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    df.to_csv(csv_file, index=False)
    
    loaded_df = data_loader(csv_file)
    assert loaded_df.shape == (3, 2)