import pandas as pd
from process_data import data_split, data_loader

def test_data_split_returns_train_test(sample_csv_path):
    df = data_loader(sample_csv_path)
    train, test = data_split(sample_csv_path, test_size=0.3, random_state=0)
    assert isinstance(train, pd.DataFrame) and isinstance(test, pd.DataFrame)
    assert len(train) + len(test) == len(df)
    assert train.shape[1] == df.shape[1] == test.shape[1]