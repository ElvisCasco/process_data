import pandas as pd
from process_data import data_binary

def test_data_binary_gender_column():
    df = pd.DataFrame({"gender": ["M", "F", "m", "f", "Male", "Female", None, "unknown"]})
    out = data_binary(df, "gender")
    # Known values map to 0/1, unknown/None map to <NA>
    assert set(out["gender"].dropna().unique()) <= {0, 1}
    assert str(out["gender"].dtype) == "Int64"

import pandas as pd
from process_data import data_binary

def test_data_binary_gender_column():
    df = pd.DataFrame({"gender": ["M", "F", "m", "f", "Male", "Female", None, "unknown"]})
    out = data_binary(df, "gender")
    # Known values map to 0/1, unknown/None map to <NA>
    assert set(out["gender"].dropna().unique()) <= {0, 1}
    assert str(out["gender"].dtype) == "Int64"