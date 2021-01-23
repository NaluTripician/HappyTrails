import urllib.request
import json
import sys

def calcDistance(possible_origins, possible_dest):
    distance_dict = {}
    apiKey = 'AIzaSyBpXEqVODCBRNApfwdQjg_LsPLL_UUyCbU'
    urlStem = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    destinations = 'destinations=place_id:'
    origins = 'origins='

    for x in possible_origins:
        origins += x
        if possible_origins.index(x) != len(possible_origins) - 1:
            origins += '|'

    for x in possible_dest:
        destinations += x
        #if possible_dest.index(x) != len(possible_dest) - 1:
            #destinations += '|'

    params = 'units=imperial&' + origins + '&' + destinations + '&mode=walking' + '&key=' + apiKey

    request = urlStem + params

    print(request)

    response = urllib.request.urlopen(request).read()

    distances = json.loads(response)

    for x in distances['rows']:
        ind = distances['rows'].index(x)
        origin_id = possible_origins[ind]
        min_dist = 0
        for y in x['elements']:
            ind2 = x['elements'].index(y)
            if ind2 == 0:
                min_dist = y['distance']['value']
            elif y['distance']['value'] < min_dist:
                min_dist = y['distance']['value']
            else:
                pass
        distance_dict[origin_id] = min_dist

    return distance_dict

calcDistance(['place_id:ChIJW-fzPFPa5okRZ5ja8hJQhJ0', 'place_id:ChIJ74xBa47b5okRLf1gMWs5d8w'], "ChIJm7aRpr_b5okRUjMDYPutIXQ")
