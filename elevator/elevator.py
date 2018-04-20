class Elevator():
    def __init__(self):
        self._floor = 0
        self._visitors = set()
        self._dir = 1
        self._running = True

    @property
    def floor(self):
        return self._floor

    @property
    def visitors(self):
        return self._visitors

    @property
    def running(self):
        return self._running

    def get_in(self, visitor):
        self._visitors.add(visitor)

    def get_out(self, visitor):
        self._visitors.discard(visitor)

    def run(self, floors):
        self._floor += self._dir
        if self._floor is floors-1:
            self._dir = -1
        if self._floor < 0:
            self._running = False


if __name__ == '__main__':
    e = Elevator()
    for n in range(20):
        print(e.run(5))
