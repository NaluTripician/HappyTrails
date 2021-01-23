"""
Ranks how "desirable" a place is based on type, price level, rating, and distance from the original route
"""

def rank(places,dist):
    type_list = ['amusement_park', 'aquarium', 'art_gallery', 'bakery', 'bicycle_store', 'book_store', 'bowling_alley', 'cafe', 'clothing_store', 'library', 'movie_theater', 'museum', 'park', 'shopping_mall', 'stadium', 'tourist_attraction', 'zoo', 'food', 'landmark', 'natural_feature', 'point_of_interest', 'town_square']
    for place_id in places:
        rank = 0
        keys = places[place_id].keys()
        if ('types' in keys): #check if type is in type_list. if it isn't, rank += 5
            for type in (places[place_id]['types']):
                if type not in type_list
                    rank += 5
        if ('price_level' in keys):
            rank += 2*(places[place_id]['price_level'])
        if ('rating' in keys):
            rank += 5*(1//(places[place_id]['rating']))
#        distance = jack's code
        rank+= 3*(places[place_id]['distance']/dist)
        places[place_id]['rank'] = rank
    return([(k,v) for k, v in sorted(places.items(), key=lambda item: item[1]['rank'])])
