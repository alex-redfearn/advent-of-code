from utils.read_write import ReadWrite
from game import Game


def main():
    rows = ReadWrite.read_file_rows("day-6/input/input.txt")
    map = create_map(rows)
    game = Game(map[0])
    
    loops = game.loop_count(map[1])
    print(loops)

def create_map(rows) -> tuple:
    map = {}
    start = (0, 0)

    for row_index, row in enumerate(rows):
        for col_index, char in enumerate(row):
            if char == "^":
                start = (row_index, col_index)
            map[(row_index, col_index)] = char

    return (map, start)


if __name__ == "__main__":
    main()
