from direction import Direction

class Position:
    
    def __init__(self, coordinates: tuple[int, int], direction: Direction):
        self._coordinates = coordinates
        self._direction = direction

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def direction(self):
        return self._direction
