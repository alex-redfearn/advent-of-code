from utils.read_write import ReadWrite
from equation import Equation


def main():
    rows = ReadWrite.read_file_rows("day-7/input/input.txt")
    equations = parse(rows)
    operators = ["+", "*"]

    total = 0
    for target, numbers in equations.items():
        if Equation.is_any_match(target, numbers, operators):
            total += target

    ReadWrite.write("day-7/output/output.txt", [total])


def parse(rows) -> dict:
    d = {}

    for row in rows:
        split = row.split(":")
        key = int(split[0])
        value = list(map(int, split[1].strip().split(" ")))
        d[key] = value

    return d


if __name__ == "__main__":
    main()
