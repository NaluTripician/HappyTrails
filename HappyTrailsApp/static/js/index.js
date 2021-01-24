function initMap(routeRequest){
    console.log("got into init map");
    var directionsService = new google.maps.DirectionsService();
    var directionsRenderer = new google.maps.DirectionsRenderer();



    const uluru = {lat: -25.344, lng: 131.036 };

    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: uluru,
    });
    const marker = new google.maps.Marker({
        position: uluru,
        map: map,
    });

    directionsRenderer.setMap(map);
    console.log("got into calcroute");
    directionsService.route(routeRequest, function(result, status) {
        if (status == 'OK'){
            directionsRenderer.setDirections(result);
        }
    });
}