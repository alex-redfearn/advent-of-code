class ReadWrite:

    @staticmethod
    def read_file_rows(path: str):
        data = []

        with open(path, "r") as file:
            for line in file:
                row = line.strip()
                data.append(row)

        return data

    @staticmethod
    def read_file_columns_numbers(path: str, separator: str, columns: int):
        data = [[] for _ in range(columns)]

        with open(path, "r") as file:
            for line in file:
                cols = line.strip().split(separator)
                for i in range(columns):
                    data[i].append(int(cols[i]))

        return data

    @staticmethod
    def read_file_rows_numbers(path: str, separator: str):
        data = []

        with open(path, "r") as file:
            for line in file:
                row = list(map(int, line.strip().split(separator)))
                data.append(row)

        return data

    @staticmethod
    def write(path: str, lines: list):
        with open(path, "w") as file:
            for line in lines:
                file.write(str(line) + "\n")
