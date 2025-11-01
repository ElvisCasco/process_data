# e. Generate dummies for ethnicity column (One hot encoding).

import pandas as pd
from typing import Sequence

def data_encoding(df: pd.DataFrame, columns: Sequence[str]) -> pd.DataFrame:
    """
    One-hot encode only the specified columns.
    Pass columns as a list, e.g., ["ethnicity"].
    """
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise KeyError(f"Columns not found: {missing}")
    return pd.get_dummies(df, columns=list(columns), drop_first=False, dtype=int)
