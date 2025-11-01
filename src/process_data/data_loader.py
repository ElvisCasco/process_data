# a. Load the data

from pathlib import Path
from typing import Union
import pandas as pd

def data_loader(file_name: Union[str, Path]) -> pd.DataFrame:
    file_name = Path(file_name)
    data = pd.read_csv(file_name)
    print(f"Data loaded successfully. Shape: {data.shape}")
    return data