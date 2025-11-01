import pandas as pd
from process_data import data_encoding

def test_data_encoding_ethnicity_only():
    df = pd.DataFrame(
        {
            "ethnicity": ["A", "B", "A", "C"],
            "age": [20, 30, 25, 40],
        }
    )
    out = data_encoding(df, columns=["ethnicity"])
    # Original non-encoded columns remain
    assert "age" in out.columns
    # Dummies created for each level of ethnicity
    assert {"ethnicity_A", "ethnicity_B", "ethnicity_C"}.issubset(out.columns)
    # Row count unchanged
    assert len(out) == len(df)
# ...existing code...