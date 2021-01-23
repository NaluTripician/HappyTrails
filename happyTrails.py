import urllib.request
import json
import random
import sys
import route from requestRoute
import rank from rank

def getNumStops(dist):
    if dist < 1999:
        return 2
    elif dist < 9999:
        return dist%1000
    elif(dist <199999):
        return 2
    else:
        return dist%100000

def main(start,end,apiKey,mode):

    path,places,dist = route(start,end,apiKey,mode)

    numberOfStops = getNumStops(dist)
    finalDestinations = rank(places)[:numberOfStops]

    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

    navReq = 'origin={}&destination={}&mode={}&key={}&waypoints:optimize:true'.format(start.replace(" ","+"),end.replace(" ","+"),mode.replace(" ","+"),apiKey)

    for poi in finalDestinations:
        naviReq += '|' + poi

    request = endpoint+navReq
    response = urllib.request.urlopen(request).read()

    return json.loads(response)

if __name__ == '__main__':
  main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
