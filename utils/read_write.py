class ReadWrite:

    @staticmethod
    def read_file_separated_numbers(path: str, separator: str, columns: int):
        data = [[] for _ in range(columns)]

        with open(path, 'r') as file:
            for line in file:
                cols = line.strip().split(separator)
                for i in range(columns):
                    data[i].append(int(cols[i]))

        return data
    
    @staticmethod
    def write(path: str, lines: list):
        with open(path, 'w') as file:
            for line in lines:
                file.write(str(line) + '\n')

