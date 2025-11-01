import pandas as pd
from process_data import data_fill_nans

def test_data_fill_nans_selected_columns_only():
    df = pd.DataFrame(
        {
            "height": [170.0, None, 180.0],
            "weight": [70.0, 80.0, None],
            "note": ["a", "b", None],  # non-numeric should be unchanged
        }
    )
    cols = ["height", "weight"]
    out = data_fill_nans(df, columns=cols)

    # Specified numeric columns should have no NaNs after fill
    assert out[cols].isna().sum().sum() == 0

    # Unspecified/non-numeric column remains unchanged (still has NaN)
    assert out["note"].isna().sum() == 1