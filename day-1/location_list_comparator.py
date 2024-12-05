from collections import Counter


class LocationListComparator:

    def __init__(self, left: list[int], right: list[int]):
        self.left = sorted(left)
        self.right = sorted(right)

    def compare_distance(self):
        score = 0

        for i in range(len(self.left)):
            score += abs(self.left[i] - self.right[i])

        return score

    def compare_similarity(self):
        score = 0

        occurrences = Counter(self.right)

        for i in range(len(self.left)):
            id = self.left[i]
            occurrence = occurrences[id]
            score += id * occurrence

        return score
