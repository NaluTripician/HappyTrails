from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from happyTrails import main
import json

index = 'HappyTrailsApp/index.html'

def index(request):
    if request.method == 'POST':
        place_list,addressList = main(
        request.POST['origin'],
        request.POST['end'],
        "AIzaSyBpXEqVODCBRNApfwdQjg_LsPLL_UUyCbU",
        request.POST['transport_mode'].upper(),
        )

        print(place_list)
        print("addressList:", addressList)
        print("address liost json:", json.dumps(addressList))
        newAddressList = []
        for address in addressList:
            newAddressList.append({
                'name': address[0],
                'address': address[1]
            })

        # newAddressList = json.dumps(newAddressList)
        
        print(newAddressList)
        place_list = place_list[:5]
        print("AFTER:", place_list)
        

        routeRequest = {
            
            'origin': request.POST['origin'],
            'destination': request.POST['end'],
            'waypoints': [{'stopover': True, 'location': {'placeId': waypoint_id}} for waypoint_id in place_list],
            'travelMode': request.POST['transport_mode'].upper(),
            'optimizeWaypoints': True,
        }
        return render(request, 'HappyTrailsApp/index.html', {
            'routeRequest': json.dumps(routeRequest),
            'addressList': newAddressList,
        })
    else:
        context = {
            'routeRequest': 'No Route',
            'addressList': [],

        }
        return render(request, 'HappyTrailsApp/index.html', context)

def nalu(request, question_id):
    return HttpResponse("Nalu Sucks %s Butts." % question_id)

def locations(request):

# THIS PIECE OF CODE ISNT CALLLED
    print("above the call to main")
    place_list, addressList = main(
        request.POST['origin'],
        request.POST['end'],
        "AIzaSyBpXEqVODCBRNApfwdQjg_LsPLL_UUyCbU",
        request.POST['transport_mode'].upper(),
        )

    print("place list:", place_list)
    print("addressList:", addressList)
    
    
    # place_list = place_list[:5]
    # print("AFTER:", place_list)
    

    routeRequest = {
        
        'origin': request.POST['origin'],
        'destination': request.POST['end'],
        'waypoints': [{'stopover': True, 'location': {'placeId': waypoint_id}} for waypoint_id in place_list],
        'travelMode': request.POST['transport_mode'].upper(),
        'optimizeWaypoints': True,
    }
    return render(request, 'HappyTrailsApp/index.html', {
        'routeRequest': json.dumps(routeRequest),
    })