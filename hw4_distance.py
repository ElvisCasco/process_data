from geopy.distance import geodesic

def compute_distance(coord_list):
    coord_distances = []
    for coord_pair in coord_list:
        distance = geodesic(coord_pair[0], coord_pair[1]).km
        coord_distances.append(distance)
    return coord_distances

coords = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]

print(f"{compute_distance(coords)} km")