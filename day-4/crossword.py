class Crossword:

    def __init__(self, puzzle: list[str]):
        self.puzzle = puzzle
        self.length = len(puzzle)

    def occurences(self, word) -> int:
        return self.__count(word)

    def x_occurrences(self, word) -> int:
        """
        What is an x occurrence you ask?
        An x word is a word in the shape of an X.
        Each side of the X can be forwards or backwords.
        For example the word MAS:
        [M.S]
        [.A.]
        [M.S]

        :return: count of the occurrences
        """
        return self.__x_count(word)

    def __count(self, word):
        count = 0

        for row, value in enumerate(self.puzzle):
            for col in range(len(value)):
                if self.__horizontal(row, col, word):
                    count += 1

                if self.__vertical(row, col, word):
                    count += 1

                if self.__diagonal_right(row, col, word):
                    count += 1

                if self.__diagonal_left(row, col, word):
                    count += 1

        return count

    def __x_count(self, word):
        count = 0

        for row, value in enumerate(self.puzzle):
            for col in range(len(value)):
                if self.__diagonal_right(row, col, word) and self.__diagonal_left(
                    row, col + 2, word
                ):
                    count += 1

        return count

    def __horizontal(self, r, c, word) -> bool:
        occurance = False

        if c <= len(self.puzzle[r]) - len(word):
            result = ""
            for i in range(len(word)):
                result += self.puzzle[r][c + i]
            occurance = result == word or result == word[::-1]

        return occurance

    def __vertical(self, r, c, word) -> bool:
        occurance = False

        if r <= self.length - len(word):
            result = ""
            for i in range(len(word)):
                result += self.puzzle[r + i][c]
            occurance = result == word or result == word[::-1]

        return occurance

    def __diagonal_right(self, r, c, word) -> bool:
        occurance = False

        if c <= len(self.puzzle[r]) - len(word) and r <= self.length - len(word):
            result = ""
            for i in range(len(word)):
                result += self.puzzle[r + i][c + i]
            occurance = result == word or result == word[::-1]

        return occurance

    def __diagonal_left(self, r, c, word) -> bool:
        occurance = False

        if c >= len(word) - 1 and r <= self.length - len(word):
            result = ""
            for i in range(len(word)):
                result += self.puzzle[r + i][c - i]
            occurance = result == word or result == word[::-1]

        return occurance
