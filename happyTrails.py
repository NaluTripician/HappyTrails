import urllib.request
import json
import random
import sys
import route from requestRoute
import rank from rank

def main(start,end,apiKey,mode):

    path,places = route(start,end,apiKey,mode)

    #ranking stuff will go here

    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

    navReq = 'origin={}&destination={}&mode={}&key={}&waypoints:optimize:true'.format(start.replace(" ","+"),end.replace(" ","+"),mode.replace(" ","+"),apiKey)

    for poi in finalDestinations:
        naviReq += '|' + poi

    request = endpoint+navReq
    response = urllib.request.urlopen(request).read()

    return json.loads(response)

if __name__ == '__main__':
  main(sys.argv[1],sus.argv[2],sys.argv[3],sys.argv[4])
