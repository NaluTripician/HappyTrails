import urllib.request
import json
import random
import sys
from requestRoute import route
from rank import rank
from distanceCalculator import calcDistance

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
    finalDestinations = rank(calcDistance(places,path),dist)[:numberOfStops]

    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

    navReq = 'origin={}&destination={}&mode={}&key={}&waypoints:optimize:true'.format(start.replace(" ","+"),end.replace(" ","+"),mode.replace(" ","+"),apiKey)

    for poi in finalDestinations:
        navReq += '|' + poi[0]

    request = endpoint+navReq
    response = urllib.request.urlopen(request).read()
    happyTrail = json.loads(response)

    with open('happytrail.txt','w') as json_file:
        json.dump(happyTrail,json_file)

    return happyTrail

if __name__ == '__main__':
  main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
