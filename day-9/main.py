from utils.read_write import ReadWrite
from disk_one import DiskOne
from disk_two import DiskTwo


def main():
    rows = ReadWrite.read_file_rows("day-9/input/input.txt")
    disk_map = rows[0]

    disk_one = DiskOne(disk_map)
    disk_one.compress()
    disk_one_size = disk_one.size()

    disk_two = DiskTwo(disk_map)
    disk_two.compress()
    disk_two_size = disk_two.size()
    print(disk_two_size)

    ReadWrite.write("day-9/output/output.txt", [disk_one_size, disk_two_size])


def create_map(rows) -> list[list]:
    return [list(row) for row in rows]


if __name__ == "__main__":
    main()
