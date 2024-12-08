from utils.read_write import ReadWrite
from dag import Dag


def main():
    rows = ReadWrite.read_file_rows("day-5/input/input.txt")
    edges = parse_edges(rows)
    nodes_list = parse_nodes_list(rows)

    ReadWrite.write(
        "day-5/output/output.txt", [sum_middle_nodes(Dag(edges), nodes_list)]
    )


def sum_middle_nodes(dag, nodes_list):
    sorted_list = []
    for nodes in nodes_list:
        sorted = dag.sort(nodes)
        if sorted != nodes:
            sorted_list.append(dag.sort(nodes))

    middle_numbers = [sublist[len(sublist) // 2] for sublist in sorted_list]

    return sum(middle_numbers)


def parse_edges(rows) -> list[tuple]:
    edges = []

    for line in rows:
        if line == "":
            break
        else:
            split = line.split("|")
            edges.append((int(split[0]), int(split[1])))

    return edges


def parse_nodes_list(rows) -> list[int]:
    nodes = []
    lenght = len(rows)

    for i in range(lenght):
        row = rows[lenght - 1 - i]
        if row == "":
            break
        else:
            nodes.append([int(x) for x in row.split(",")])

    return nodes


if __name__ == "__main__":
    main()
