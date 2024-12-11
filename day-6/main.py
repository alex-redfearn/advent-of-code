from utils.read_write import ReadWrite
from game import Game
from position import Position
from direction import Direction


def main():
    rows = ReadWrite.read_file_rows("day-6/input/input.txt")
    map = create_map(rows)
    game = Game(map[0])
    
    #print(game.loop_count(map[1]))
    
    loops = game.loop_count(Position(map[1], Direction.UP))
    print(loops)
    
    # final_position = game.play(Position(map[1], Direction.UP))
    # print(final_position[0])
    # print(len(final_position[1]))
    
    # unique_moves = sum(1 for value in game.map.values() if value == game.FOOT_PRINT)
    # print(unique_moves)
    
    
    
    
    

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
