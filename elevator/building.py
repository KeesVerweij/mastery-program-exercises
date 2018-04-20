from visitor import Visitor
from elevator import Elevator


class Building:
    def __init__(self, floors=5, visitors=5):
        self._floors = floors
        self._visitors = self.create_visitors(visitors)
        self._elevator = Elevator()

    @property
    def floors(self):
        return self._floors

    def create_visitors(self, n):
        visitors = {Visitor(x) for x in range(n)}
        for visitor in visitors:
            visitor.plan_trip(self._floors)
        return visitors

    def work_day(self):
        while self._elevator.running:
            print('elevetor floor: ' + str(self._elevator.floor), end=", ")
            for visitor in self._visitors:
                visitor.into_elevator(self._elevator)
                visitor.out_of_elevator(self._elevator)
            print("visitors in elevator: " +
                  str([visitor.id for visitor in self._elevator.visitors]))
            self._elevator.run(self._floors)
            print('---')

    def __str__(self):
        return "a building with " + str(self._floors) + \
            " floors and visitors: " + str(self._visitors)


if __name__ == "__main__":
    building = Building()
    building.work_day()
