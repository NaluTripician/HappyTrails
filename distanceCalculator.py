import geopy.distance
import numpy as np
from requestRoute import route
import itertools

def calcDistance(possible_origins, possible_dest):
    out_arr = []
    for x in possible_origins:
        out_arr.append(calcDistance2(x, possible_dest))
    return out_arr


def calcDistance2(possible_origins, possible_dest):
    """
    Calculates distances from the Google Maps route for points of interest

    possible_origins: a dictionary of place IDs and features of the POIs
    possible_dest: a list of tuples representing coordinates from along the route

    returns: distance_dict, a modified version of the origins dictionary with distances added to
    represent the shortest distance from the original route to the POI
    """
    for x in possible_origins:
        coords_1 = possible_origins[x]['coords']
        min_dist = 0
        i = 0
        for y in possible_dest:
            coords_2 = y
            dist = geopy.distance.distance(coords_1, coords_2).meters
            if i == 0:
                min_dist = dist
            elif dist < min_dist:
                min_dist = dist
            else:
                pass
            i+=1
        possible_origins[x]['distance'] = min_dist

    return possible_origins
