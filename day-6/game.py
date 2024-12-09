from direction import Direction


class Game:

    EMPTY_SPACE = "."
    OBSTACLE = "#"
    FOOT_PRINT = "X"

    def __init__(self, map: dict[tuple, str], start: tuple[int, int]):
        self.map = map
        self.coordinates = list(start)
        self.current_direction = Direction.UP
        self.game_over = False

    def play(self) -> int:
        while self.game_over == False:

            # Mark current pos
            self.map[(self.coordinates[0], self.coordinates[1])] = self.FOOT_PRINT

            # Get next pos
            next_row = self.coordinates[0] + self.current_direction.row
            next_col = self.coordinates[1] + self.current_direction.col

            next_value = self.map.get((next_row, next_col))

            if next_value == self.EMPTY_SPACE or next_value == self.FOOT_PRINT:
                self.move(next_row, next_col)
                continue

            if next_value == self.OBSTACLE:
                self.current_direction = Direction.turn_right(self.current_direction)
                continue

            if next_value is None:
                self.game_over = True
                break

        # Returns a count of the unique moves made by the player
        return sum(1 for value in self.map.values() if value == self.FOOT_PRINT)

    def move(self, row, col):
        self.coordinates = [row, col]
