"""
Ranks how "desirable" a place is based on type, price level, rating, and distance from the original route
"""

def rank(place_dict)
    types = [amusement_park, aquarium, art_gallery, bakery, bicycle_store, book_store, bowling_alley, cafe, clothing_store, library, movie_theater, museum, park, shopping_mall, stadium, tourist_attraction, zoo, food, landmark, natural_feature, point_of_interest, town_square]
    for (key,val) in place_dict
        (key,val) = (place_id, (lat, lng, rating, placeID, type, price_level, website))
#        distance = jack's code
        if type not in types:
            type_val = 5
        else:
            type_val = 0
        rank = (2*price_level) + (5*(1//rating)) + (4*distance) + type_val
        (key,val) = (key, rank)
    return({key: val for key, val in sorted(place_dict.items(), key=lambda item: item[1])})
