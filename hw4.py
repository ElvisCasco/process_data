##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

def count_simba(list):
    count = 0
    for item in list:
        count += item.count("Simba")
    return count

list = ["Simba and Nala are lions.", 
              "I laugh in the face of danger.", 
              "Hakuna matata", 
              "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 

print(count_simba(list))
    

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


# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

from geopy.distance import geodesic

def compute_distance(coord_list):
    coord_distances = []
    for coord_pair in coord_list:
        distance = geodesic(coord_pair[0], coord_pair[1]).km
        coord_distances.append(distance)
    return coord_distances

coords = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]

print(f"{compute_distance(coords)} km")


#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

def sum_general_int_list(general_list):
    total = 0
    for item in general_list:
        if isinstance(item, list):
            total += sum_general_int_list(item)
        else:
            total += item
    return total

sample_list = [[1], 2, 3, [4, [5], [6, 7, [8,9]], 10], 1]

print(sum_general_int_list(sample_list))