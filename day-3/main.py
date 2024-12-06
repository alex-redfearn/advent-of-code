from utils.read_write import ReadWrite
from corrupt_multiplication import CorruptMultiplication


def main():
    corrupted_multiplications = ReadWrite.read_file_rows("day-3/input/input.txt")
    ReadWrite.write(
        "day-3/output/output.txt",
        [CorruptMultiplication("".join(corrupted_multiplications)).multiply()],
    )


if __name__ == "__main__":
    main()
