from random import randrange


class Visitor:
    def __init__(self, id):
        self._id = id
        self._trip = [0, 0]

    @property
    def id(self):
        return self._id

    @property
    def trip(self):
        return self._trip

    def plan_trip(self, floors):
        floor_start = randrange(floors)
        floor_end = randrange(floors)
        while floor_end is floor_start:
            floor_end = randrange(floors)
        trip = (floor_start, floor_end)
        self._trip = trip

    def __str__(self):
        return "visitor " + str(self._id)


if __name__ == "__main__":
    v = Visitor(1)
    print(v.plan_trip(5))
