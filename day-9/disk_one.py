from collections import deque


class DiskOne:

    def __init__(self, map):
        self._map = map

    @staticmethod
    def _parse(disk_map):
        map = []
        index = 0
        for i in range(len(disk_map)):
            value = (str(i // 2), ".")
            map.extend([value[index] for _ in range(int(disk_map[i]))])
            index = 1 - index

        return map

    def compress(self):
        self._map = self._parse(self._map)

        compressed_map = self._map
        space_compressed = 0

        # find the first value from the right
        for i in range(len(compressed_map) - 1, -1, -1):
            value = compressed_map[i]

            if value == ".":
                continue

            # Find the first free space from the left
            for j in range(space_compressed, i):
                if compressed_map[j] == ".":
                    # Move into free space
                    compressed_map[j] = value
                    compressed_map[i] = "."
                    space_compressed = j + 1
                    break

        self._map = compressed_map

    def size(self):
        size = 0

        for i in range(len(self._map)):
            value = self._map[i]
            if value == ".":
                break

            size += i * int(value)

        return size
