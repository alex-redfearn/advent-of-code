from utils.read_write import ReadWrite
from location_list_comparator import LocationListComparator


def main():
    # format, two columns of ids seperated by three spaces.
    location_ids = ReadWrite.read_file_columns_numbers(
        "day-1/input/input.txt", "   ", 2
    )

    comparison = compare_locations(location_ids)
    ReadWrite.write("day-1/output/output.txt", comparison)


def compare_locations(lists: list[list[int]]):
    comparator = LocationListComparator(lists[0], lists[1])

    distance = comparator.compare_distance()
    similarity = comparator.compare_similarity()

    return [distance, similarity]


if __name__ == "__main__":
    main()
