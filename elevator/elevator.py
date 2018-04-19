class Elevator():
    def __init__(self):
        self._floor = 0
        self._visitors = []
        self._dir = 1

    @property
    def floor(self):
        return self._floor

    def run(self, floors):
        self._floor += self._dir
        if self._floor <= 0:
            self._dir = 1
        elif self._floor >= floors:
            self._dir = -1
        return self._floor


if __name__ == '__main__':
    e = Elevator()
    for n in range(20):
        print(e.run(5))
