from collections import defaultdict
from functools import cmp_to_key


class Dag:

    def __init__(self, edges):
        self.graph = self.__graph(edges)

    def __graph(self, edges) -> defaultdict:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)

        return graph

    def sort(self, nodes):

        def compare(current, next):
            if current in self.graph[next]:
                return 1
            elif next in self.graph[current]:
                return -1
            else:
                return 0

        return sorted(nodes, key=cmp_to_key(compare))
