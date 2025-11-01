import pandas as pd
from process_data import data_loader

def test_can_load_sample_csv(sample_csv_path):
    df = data_loader(sample_csv_path)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty