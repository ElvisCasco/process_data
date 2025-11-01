import pandas as pd
from process_data import data_remove_nans

def test_data_remove_nans_specific_columns():
    df = pd.DataFrame({
        "age": [20, None, 30],
        "gender": ["M", "F", None],
        "ethnicity": ["A", "B", "C"],
        "height": [170, 160, 180],
    })
    cols = ["age", "gender", "ethnicity"]
    out = data_remove_nans(df, columns=cols)

    # Only rows with complete values in the specified columns should remain
    assert out.shape[0] == 1
    assert out[cols].isna().sum().sum() == 0