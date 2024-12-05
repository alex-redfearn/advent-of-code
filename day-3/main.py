from utils.read_write import ReadWrite
from corrupt_multiplication import CorruptMultiplication


def main():
    total = 0

    # This should be all one big line, not meant to be split into lines.
    corrupted_multiplications = ReadWrite.read_file_rows("day-3/input/input.txt")
    total = CorruptMultiplication("".join(corrupted_multiplications)).multiply()
    ReadWrite.write("day-3/output/output.txt", [total])


if __name__ == "__main__":
    main()
