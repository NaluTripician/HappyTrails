"""
Ranks how "desirable" a place is based on type, price level, rating, and distance from the original route
"""

def rank(places,dist):
    type_list = ['amusement_park', 'aquarium', 'art_gallery', 'bakery', 'bicycle_store', 'book_store', 'bowling_alley', 'cafe', 'clothing_store', 'library', 'movie_theater', 'museum', 'park', 'shopping_mall', 'stadium', 'tourist_attraction', 'zoo', 'food', 'landmark', 'natural_feature', 'town_square']
    bad_types = ['accounting', 'airport', 'atm', 'bank', 'bus_station', 'car_dealer', 'car_rental', 'car_repair', 'car_wash', 'courthouse', 'dentist', 'electrician', 'fire_station', 'gas_station', 'gym', 'hardware_store', 'hospital', 'insurance_agency', 'laundry', 'light_rail_station', 'local_government_office', 'locksmith', 'moving_company', 'pharmacy', 'physiotherapist', 'plumber', 'police', 'primary_school', 'real_estate_agency', 'roofing_contractor', 'secondary_school', 'subway_station', 'taxi_stand', 'train_station', 'transit_station', 'veterinary_care', 'colloquial_area', 'continent', 'country', 'finance', 'general_contractor', 'health', 'locality', 'neighborhood', 'postal_code', 'postal_code_prefix', 'postal_code_suffix', 'postal_town', 'premise', 'room', 'sublocality', 'subpremise', 'administrative_area_level_1', 'administrative_area_level_2']
    print(len(places.keys()))
    for place_id in places:
        avail = True
        rank = 0
        keys = places[place_id].keys()
        if ('types' in keys): #check if type is in type_list. if it isn't, rank += 5
            for type in (places[place_id]['types']):
                if type in bad_types:
                    places.pop(place_id, None)
                    avail = False
                    print('break1')
                    break
                elif type not in type_list:
                    rank += 3
        if avail == False:
            print('break2')
            break
        if ('price_level' in keys):
            rank += 2*(places[place_id]['price_level'])
        if ('rating' in keys):
            rank += 5*(1//(places[place_id]['rating']))
        rank+= 3*(places[place_id]['distance']/dist)
        places[place_id]['rank'] = rank
    print(len(places.keys()))
    return([(k,v) for k, v in sorted(places.items(), key=lambda item: item[1]['rank'])])
