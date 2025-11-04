# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

import pandas as pd

def get_day_month_year(date_list):
    days, months, years = [], [], []
    for d,m,y in date_list:
        days.append(int(d))
        months.append(int(m))
        years.append(int(y))
    return pd.DataFrame({'day': days, 'month': months, 'year': years})

dates = [["22","05","1992"], ["25","05","1958"], ["06","22","1961"], ["08","04","1995"]]

print(get_day_month_year(dates))

