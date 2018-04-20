from random import randrange


class Visitor:
    def __init__(self, id):
        self._id = id
        self._trip = [0, 0]
        self._trip_finished = False

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

    def into_elevator(self, elevator):
        start_floor = self.trip[0]
        if start_floor is elevator.floor \
                and self not in elevator.visitors \
                and self._trip_finished is False:
            elevator.get_in(self)
            print("person " + str(self.id), end=" got into the elevator, ")

    def out_of_elevator(self, elevator):
        end_floor = self.trip[1]
        if end_floor is elevator.floor and self in elevator.visitors:
            elevator.get_out(self)
            self._trip_finished = True
            print("person " + str(self.id), end=" got out of the elevator, ")

    def __str__(self):
        return "visitor " + str(self._id)


if __name__ == "__main__":
    v = Visitor(1)
    print(v.plan_trip(5))
