import urllib.request
import json
import random
import sys
from requestRoute import route
from rank import rank
from distanceCalculator import calcDistance

def main(start,end,apiKey,mode):

    path,places,dist = route(start,end,apiKey,mode)

    finalDestinations = rank(calcDistance(places,path),dist)

    happyTrail = []
    nameAddress = []
    for poi in finalDestinations:
        if poi is not None:
            happyTrail.append(poi[0])
            nameAddress.append((poi[1]['name'],poi[1]['formatted_address']))

    return happyTrail,nameAddress

if __name__ == '__main__':
  main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
