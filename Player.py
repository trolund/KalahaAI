from xxlimited import Null

import PlaceEnum


class Player:
    name = Null
    place: PlaceEnum = Null

    def __init__(self, name, place):
        self.name = name
        self.place = place

