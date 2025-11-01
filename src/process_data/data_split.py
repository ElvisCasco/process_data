# b. Split the data between train and test. 
# # (you can use train_test_split from sklearn or any other way)

from typing import Tuple, Union
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from .data_loader import data_loader

def data_split(file_name: Union[str, Path], test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = data_loader(file_name)
    train, test = train_test_split(data, test_size=test_size, random_state=random_state)
    return train, test