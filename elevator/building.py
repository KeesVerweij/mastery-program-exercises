from visitor import Visitor
from elevator import Elevator


class Building:
    def __init__(self, floors=5, visitors=10):
        self._floors = floors
        self._visitors = self.create_visitors(visitors)
        self._elevator = Elevator()

    @property
    def floors(self):
        return self._floors

    def create_visitors(self, n):
        visitors = [Visitor(x) for x in range(n)]
        for visitor in visitors:
            visitor.plan_trip(self._floors)
        return visitors

    def on_same_floor(self):
        elevator_floor = self._elevator.floor
        for visitor in self._visitors:
            start_floor = visitor.trip[0]
            if start_floor is elevator_floor:
                print('visitor ' + str(visitor.id) + ' is on the same floor as the elevator!')

    def work_day(self):
        for step in range(11):
            print(self._elevator.floor)
            self.on_same_floor()
            self._elevator.run(self._floors)

    def __str__(self):
        return "a building with " + str(self._floors) + " floors and visitors: " + str(self._visitors)


if __name__ == "__main__":
    building = Building()
    building.work_day()
