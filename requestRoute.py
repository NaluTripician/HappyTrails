import urllib.request
import json
import sys

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
apiKey = 'AIzaSyBpXEqVODCBRNApfwdQjg_LsPLL_UUyCbU'

origin = sys.argv[1]
destination = sys.argv[2]

navReq = 'origin={}&destination={}&key={}'.format(origin.replace(" ","+"),destination.replace(" ","+"),apiKey)

request = endpoint+navReq
response = urllib.request.urlopen(request).read()

route = json.loads(response)
