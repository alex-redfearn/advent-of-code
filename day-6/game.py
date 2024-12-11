class Game:

    EMPTY_SPACE = "."
    OBSTACLE = "#"

    def __init__(self, map: dict[tuple, str]):
        self.map = map

    def loop_count(self, start_position: tuple[int, int]) -> int:
        loop_count = 0

        # place an obstacle at every empty space and run the game.
        for coordinates in self.map.keys():
            if self.map[coordinates] == self.EMPTY_SPACE:

                self.map[coordinates] = self.OBSTACLE

                # Check if the character left the map or if it ended in a loop.
                if self.play(start_position) != [-1, -1]:
                    loop_count += 1

                self.map[coordinates] = self.EMPTY_SPACE

        return loop_count

    # Returns final coordinates
    def play(self, coordinates) -> tuple[int, int]:
        direction = (-1, 0)
        foot_steps = set()

        while True:
            
            if (coordinates, direction) in foot_steps:
                return coordinates

            foot_steps.add((coordinates, direction))

            next_coordinates = (
                coordinates[0] + direction[0],
                coordinates[1] + direction[1],
            )

            next_value = self.map.get(next_coordinates)

            if next_value is None:
                return [-1, -1]

            if self.collision(next_value):
                direction = self.turn_right(direction)
                continue

            coordinates = next_coordinates

    def collision(self, value):
        return value == self.OBSTACLE

    def turn_right(self, direction: tuple[int, int]) -> tuple[int, int]:
        direction_map = {
            (-1, 0): (0, 1),  # Up -> Right
            (0, 1): (1, 0),  # Right -> Down
            (1, 0): (0, -1),  # Down -> Left
            (0, -1): (-1, 0),  # Left -> Up
        }
        return direction_map[direction]
