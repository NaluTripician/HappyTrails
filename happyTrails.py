import urllib.request
import json
import random
import sys
from requestRoute import route
from rank import rank
from distanceCalculator import calcDistance

# def getNumStops(dist):
#     if dist < 1999:
#         return 2
#     elif dist < 9999:
#         return dist%1000
#     elif(dist <199999):
#         return 2
#     else:
#         return dist%100000

def main(start,end,apiKey,mode):

    path,places,dist = route(start,end,apiKey,mode)

    #numberOfStops = getNumStops(dist)
    finalDestinations = rank(calcDistance(places,path),dist)

    happyTrail = []
    for poi in finalDestinations:
        happyTrail.append(poi[0])
        print(poi)

    return happyTrail

if __name__ == '__main__':
  main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
