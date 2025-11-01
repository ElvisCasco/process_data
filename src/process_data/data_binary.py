# f. Create a binary variable for column gender M/F.

import pandas as pd

def data_binary(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Convert a gender column to binary 0/1.
    - M/m/Male -> 1
    - F/f/Female -> 0
    - Unrecognized or NaN -> <NA> (nullable Int64)
    """
    male_vals = {"m", "male"}
    female_vals = {"f", "female"}

    def to_bin(v):
        if pd.isna(v):
            return pd.NA
        if isinstance(v, str):
            s = v.strip().lower()
            if s in male_vals:
                return 1
            if s in female_vals:
                return 0
            return pd.NA
        if v in (1, True):
            return 1
        if v in (0, False):
            return 0
        return pd.NA

    out = df.copy()
    out[column] = out[column].map(to_bin).astype("Int64")
    return out