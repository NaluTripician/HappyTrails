"""
Ranks how "desirable" a place is based on type, price level, rating, and distance from the original route
"""

def rank(places,dist):ß
    type_list = ['amusement_park', 'aquarium', 'art_gallery', 'bakery', 'bicycle_store', 'book_store', 'bowling_alley', 'cafe', 'clothing_store', 'library', 'movie_theater', 'museum', 'park', 'shopping_mall', 'stadium', 'tourist_attraction', 'zoo', 'food', 'landmark', 'natural_feature', 'point_of_interest', 'town_square']
    for (place_id,info_dict) in places:
        rank = 0
        keys = info_dict.keys()
        if ('types' in keys): #check if type is in type_list. if it isn't, rank += 5
            if (places[place_id]['types'] not in type_list):
                rank += 5
        if ('price_level' in keys):
            rank += 2*(places[place_id]['price_level'])
        if ('rating' in keys):
            rank += 5*(1//(places[place_id]['rating']))
#        distance = jack's code
        rank+= 3*(places[placeID]['distance']/dist)
        places[place_id]['rank'] = rank
    return([key: val for key, val in sorted(place_dict.items(), key=lambda item: item[1]['rank'])])
