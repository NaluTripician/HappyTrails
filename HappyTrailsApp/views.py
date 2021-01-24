from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from happyTrails import main
import json

index = 'HappyTrailsApp/index.html'

def index(request):
    context = {
        'routeRequest': 'No Route',
    }
    return render(request, 'HappyTrailsApp/index.html', context)

def nalu(request, question_id):
    return HttpResponse("Nalu Sucks %s Butts." % question_id)

def locations(request):
    response = "You're starting at %s"
    # routeRequest = {
    #     'origin': 'Chicago, IL',
    #     'destination': 'Los Angeles, CA',
    #     'travelMode': 'DRIVING',
    #     'waypoints': [
    #         {
    #         'location': 'Joplin, MO',
    #         'stopover': False
    #         },{
    #         'location': 'Oklahoma City, OK',
    #         'stopover': True
    #         }],
        
    # }
    # print(json.dumps(routeRequest))

    place_list = main(
        request.POST['origin'],
        request.POST['end'],
        "AIzaSyBpXEqVODCBRNApfwdQjg_LsPLL_UUyCbU",
        "DRIVING"
        )

    place_list = place_list[:5]
    print(place_list)
    


    routeRequest = {
        
        'origin': request.POST['origin'],
        'destination': request.POST['end'],
        'waypoints': [{'stopover': True, 'location': {'placeId': waypoint_id}} for waypoint_id in place_list],
        'travelMode': 'DRIVING',
        'optimizeWaypoints': True,
    }
    # routeRequest = main(
    #     request.POST['origin'],
    #     request.POST['end'],
    #     "AIzaSyBpXEqVODCBRNApfwdQjg_LsPLL_UUyCbU",
    #     "WALKING"
    #     )
    return render(request, 'HappyTrailsApp/index.html', {
        'routeRequest': json.dumps(routeRequest),
    })