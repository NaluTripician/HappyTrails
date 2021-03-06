import random
"""
Ranks how "desirable" a place is based on type, price level, rating, and distance from the original route
"""
def rank2(places, dist):
    type_list = ['amusement_park', 'aquarium', 'art_gallery', 'bakery', 'bicycle_store', 'book_store', 'bowling_alley', 'cafe', 'library', 'museum', 'park', 'shopping_mall', 'stadium', 'tourist_attraction', 'zoo', 'landmark', 'natural_feature', 'town_square']
    bad_ids = []

    for place_id in places:

        rank = 0
        avail = False
        keys = places[place_id].keys()

        if ('types' in keys):
            for type in (places[place_id]['types']):
                if type in type_list:
                    avail = True
        if avail == False:
            bad_ids.append(place_id)
        else:
            if ('price_level' in keys):
                rank += 2*(places[place_id]['price_level'])
            if ('rating' in keys):
                rank += 15*(1//(places[place_id]['rating']))
            rank+= 20*(places[place_id]['distance']/dist)
            places[place_id]['rank'] = rank

    for id in bad_ids:
        del places[id]
    if len(places) == 0:
        return None
    r = random.randint(0,3)
    if r >= len(places):
        r = 0
    output = [(k,v) for k, v in sorted(places.items(), key=lambda item: item[1]['rank'])]
    return (output[r])

def rank(places,dist):
    output = []
    for place in places:
        output.append(rank2(place,dist))
    return (output)
