# c. Remove those rows that contain NaN values in the columns: 
# age, gender, ethnicity.

import pandas as pd
from typing import Sequence, Optional

def data_remove_nans(df: pd.DataFrame, columns: Optional[Sequence[str]] = None) -> pd.DataFrame:
    """
    Remove rows that contain NaN values.
    - If columns is provided, only rows with NaN in those columns are removed.
    - If columns is None (default), rows with any NaN in the DataFrame are removed.
    """
    if columns:
        return df.dropna(subset=list(columns), how="any")
    return df.dropna(axis=0, how="any")