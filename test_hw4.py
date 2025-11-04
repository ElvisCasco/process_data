
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


#test 3

from hw4 import compute_distance, sum_general_int_list
from geopy.distance import geodesic

def test_compute_distance_basic():
    coords = [
        ((41.23, 23.5), (41.5, 23.4)),
        ((52.38, 20.1), (52.3, 17.8))
    ]

    result = compute_distance(coords)

    expected_distances = [
        geodesic((41.23, 23.5), (41.5, 23.4)).km,
        geodesic((52.38, 20.1), (52.3, 17.8)).km
    ]

    for res, exp in zip(result, expected_distances):
        assert abs(res - exp) < 0.01  # Allow a small margin of error of 1%
        assert len(result) == 2
        assert all(isinstance(d, float) for d in result)

