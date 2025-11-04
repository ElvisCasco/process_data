
#test 1

from hw4_simba import count_simba

def test_count_simba_basic():
    strings = [
        "Simba and Nala are lions.",
        "I laugh in the face of danger.",
        "Hakuna matata",
        "Timon, Pumba and Simba are friends, but Simba could eat the other two."
    ]

    result = count_simba(strings)

    assert result == 3  # Simba appears 3 times 

#test 2 
from hw4_days import get_day_month_year
import pandas as pd

def test_get_day_month_year_basic():
    dates = [
        ["22", "05", "1992"],
        ["25", "05", "1958"],
        ["06", "22", "1961"],
        ["08", "04", "1995"]
    ]
    
    df = get_day_month_year(dates)

    assert isinstance(df, pd.DataFrame)

    assert list(df.columns) == ["day", "month", "year"]

    assert len(df) == 4

    assert df.loc[0, "year"] == 1992
