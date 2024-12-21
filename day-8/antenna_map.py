class AntennaMap:

    def __init__(self, map: list[list]):
        self._map = map
        self._y_length = len(map)
        self._x_length = len(map[0])
        self._antinodes = set()

    @property
    def value(self):
        return self._value

    def antinodes(self):
        return self._search()

    def _search(self):
        for r_index, r in enumerate(self._map):
            for c_index, c in enumerate(r):
                if c != ".":
                    self._antenna_match(r_index, c_index, c)

        return self._antinodes

    def _antenna_match(self, r_start, c_start, match):
        for r_index in range(r_start, len(self._map)):

            start = c_start + 1 if r_index == r_start else 0
            for c_index in range(start, len(self._map[r_index])):
                value = self._map[r_index][c_index]

                if value == match:
                    self._add_antinodes(r_start, c_start, r_index, c_index)

    def _add_antinodes(self, start_row, start_col, current_row, current_col):
        row_difference = current_row - start_row
        col_difference = current_col - start_col

        antinode_one = (start_row, start_col)
        while True:
            if self._antinode_in_map(antinode_one) == False:
                break

            self._antinodes.add(antinode_one)

            antinode_one = (
                antinode_one[0] - row_difference,
                antinode_one[1] - col_difference,
            )

        antinode_two = (current_row, current_col)
        while True:
            if self._antinode_in_map(antinode_two) == False:
                break

            self._antinodes.add(antinode_two)

            antinode_two = (
                antinode_two[0] + row_difference,
                antinode_two[1] + col_difference,
            )

    def _antinode_in_map(self, antinode: tuple) -> bool:
        return (
            antinode[0] >= 0
            and antinode[0] < self._y_length
            and antinode[1] >= 0
            and antinode[1] < self._x_length
        )

    # Required for part 1 but not part 2
    def _valid_distance_condition(self, antinode, antenna_one, antenna_two):
        # Calculate Manhattan distances from the antinode to each antenna
        distance_one = abs(antinode[0] - antenna_one[0]) + abs(
            antinode[1] - antenna_one[1]
        )
        distance_two = abs(antinode[0] - antenna_two[0]) + abs(
            antinode[1] - antenna_two[1]
        )

        # Check if one distance is exactly twice the other
        return distance_one == 2 * distance_two or distance_two == 2 * distance_one
