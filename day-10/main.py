from utils.read_write import ReadWrite
from topographic_map import TopographicMap


def main():
    rows = ReadWrite.read_file_rows("day-10/input/input.txt")
    map = create_map(rows)
    

def create_map(rows) -> dict:
    return {
        (row_index, col_index): char
        for row_index, row in enumerate(rows)
        for col_index, char in enumerate(row)
    }


if __name__ == "__main__":
    main()
