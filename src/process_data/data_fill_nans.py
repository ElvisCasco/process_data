# d. Fill NaN with the mean value of the column in the columns: 
# height, weight.

import pandas as pd
from typing import Optional, Sequence

def data_fill_nans(df: pd.DataFrame, columns: Optional[Sequence[str]] = None) -> pd.DataFrame:
    """
    Fill NaN values with the mean of each column.
    - If columns is provided, only those columns are filled (skips non-numeric).
    - If columns is None, all numeric columns are filled (backward compatible).
    """
    out = df.copy()

    if columns is None:
        cols_to_fill = out.select_dtypes(include="number").columns.tolist()
    else:
        # Validate existence; ignore non-numeric later
        missing = [c for c in columns if c not in out.columns]
        if missing:
            raise KeyError(f"Columns not found: {missing}")
        cols_to_fill = list(columns)

    for col in cols_to_fill:
        # Only fill numeric columns with mean
        if pd.api.types.is_numeric_dtype(out[col]) and out[col].isna().any():
            out[col] = out[col].fillna(out[col].mean())

    return out