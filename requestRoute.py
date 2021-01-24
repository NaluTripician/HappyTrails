import urllib.request
import json
import random
import numpy as np

def route(start,end,apiKey,mode='walking'):
    """
    requests route from googlemaps

    start/end: a string, address of start/endpoint
    mode: transportation mode, driving, walking, bicycling

    returns:    path, a list of lat,lng coords describing the path
                places, a dictionay of interesting places near the route
                dist, total length of route in meters
    """

    #request initial path
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

    navReq = 'origin={}&destination={}&mode={}&key={}&units=metric'.format(start.replace(" ","+"),end.replace(" ","+"),mode.replace(" ","+"),apiKey)

    request = endpoint+navReq
    response = urllib.request.urlopen(request).read()

    route = json.loads(response)

    route = route['routes'][0]['legs'][0]['steps']

    path = []

    dist = 0
    i = 0
    for step in route:
        if i == 0:
            startLat =  step['start_location']['lat']
            startLng =  step['start_location']['lng']

            path.append((startLat,startLng))
            i += 1

        endLat =  step['end_location']['lat']
        endLng =  step['end_location']['lng']

        path.append((endLat,endLng))

        dist += step['distance']['value']

    #chooses 4 poinsts equally spaced out based on number of instructions
    path = np.array(path)

    if(len(path)<5):
        idx = np.round(np.linspace(0, len(path) - 1, len(path))).astype(int)
    else:
        idx = np.round(np.linspace(0, len(path) - 1, 5)).astype(int)

    if(dist<10000):
        radius="500"
    elif(dist<60000):
        radius="1500"
    else:
        radius ="5000"

    endpoint='https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

    places = {}

    #Finds points of intrest near path and extracts information from them
    for point in POI:

        placeReq ='key={}&location={}&radius={}'.format(apiKey,str(point[0]) +','+str(point[1]),radius)

        request = endpoint+placeReq
        response = json.loads(urllib.request.urlopen(request).read())

        for place in response['results']:
            id = place['place_id']

            placeEndpoint = 'https://maps.googleapis.com/maps/api/place/details/json?'

            idReq ='key={}&place_id={}'.format(apiKey,id)

            placeRequest = placeEndpoint+idReq
            placeDetails = json.loads(urllib.request.urlopen(placeRequest).read())

            #Place: lat, lng, rating, placeID, type, price level, website
            places[id] = {}

            keys = placeDetails['result'].keys()

            coords = (placeDetails['result']['geometry']['location']['lat'],placeDetails['result']['geometry']['location']['lng'])
            places[id]['coords'] = coords

            if('name' in keys):
                name = placeDetails['result']['name']
                places[id]['name'] = name
            if('types' in keys):
                types = placeDetails['result']['types']
                places[id]['types'] = types
            if('price_level' in keys):
                price = placeDetails['result']['price_level']
                places[id]['price_level'] = price
            if('rating' in keys):
                rating = placeDetails['result']['rating']
                places[id]['rating'] = rating

    return path,places,dist
