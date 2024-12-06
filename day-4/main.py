from utils.read_write import ReadWrite
from crossword import Crossword


def main():
    puzzle = ReadWrite.read_file_rows("day-4/input/input.txt")

    crossword = Crossword(puzzle)
    count = crossword.occurences("XMAS")
    x_count = crossword.x_occurrences("MAS")

    ReadWrite.write("day-4/output/output.txt", [count, x_count])


if __name__ == "__main__":
    main()
