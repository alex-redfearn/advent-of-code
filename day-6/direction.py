from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    @property
    def row(self):
        return self.value[0]

    @property
    def col(self):
        return self.value[1]

    @staticmethod
    def turn_right(direction):
        directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        index = directions.index(direction)
        return directions[(index + 1) % len(directions)]