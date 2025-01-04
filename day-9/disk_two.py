from collections import deque


class DiskTwo:

    def __init__(self, map):
        self._map = self._parse(map)

    @staticmethod
    def _parse(disk_map):
        deq = deque()
        index = 0
        for i in range(len(disk_map)):
            value = (i // 2, -1)
            disk = (value[index], int(disk_map[i]))
            deq.append(disk)
            index = 1 - index

        return deq

    def compress(self):
        # Queue of tuples (value,length)
        uncompressed = self._map

        tail = deque()
        head = deque()

        while uncompressed:
            right_value = uncompressed.pop()
            tail.appendleft(right_value)

            if right_value[0] == -1:
                continue

            while uncompressed:
                left_value = uncompressed.popleft()

                # Ignore existing files
                if left_value[0] != -1:
                    head.append(left_value)
                    continue

                space = left_value[1] - right_value[1]

                # Doesn't fit, keep on looking
                if space < 0:
                    head.append(left_value)
                    continue

                # Fits with space left over
                if space > 0:
                    tail.popleft()
                    tail.appendleft((-1, right_value[1]))

                    head.append(right_value)
                    head.append((-1, space))
                    break

                # Perfect fit
                if space == 0:
                    tail.popleft()
                    tail.appendleft((-1, right_value[1]))

                    head.append(right_value)
                    break

            while head:
                uncompressed.appendleft(head.pop())

        self._map = tail
        return self._map

    def size(self):
        size = 0

        count = 0
        while self._map:
            value = self._map.popleft()

            for _ in range(value[1]):
                if value[0] != -1:
                    size += count * value[0]
                count += 1

        return size
