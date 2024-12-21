from utils.read_write import ReadWrite
from antenna_map import AntennaMap


def main():
    rows = ReadWrite.read_file_rows("day-8/input/input.txt")
    map = create_map(rows)
    antennas = AntennaMap(map)

    ReadWrite.write("day-8/output/output.txt", [len(antennas.antinodes())])


def create_map(rows) -> list[list]:
    return [list(row) for row in rows]


if __name__ == "__main__":
    main()
