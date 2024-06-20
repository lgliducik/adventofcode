def extend_matrix(matrix: list) -> list:
    new_matrix = []
    for line in matrix:
        new_matrix.append(line)
        if all(ele == "." for ele in line):
            new_matrix.append(line)

    indexes = []
    for i in range(len(matrix)):
        vert = []
        for j in range(len(matrix)):
            vert.append(matrix[j][i])
        if all(ele == "." for ele in vert):
            indexes.append(i)

    new_matrix2 = []
    for line in new_matrix:
        new_str = insert_str(line, indexes)
        new_matrix2.append(new_str)
    return new_matrix2


def insert_str(line: str, indexes: list) -> str:
    rez = ""

    slices = []
    for i in range(len(indexes)):
        if i == 0:
            start = 0
        else:
            start = indexes[i-1]

        s = line[start:indexes[i]]
        slices.append(s)

    s = line[indexes[-1]:]
    slices.append(s)

    rez = ".".join(slices)
    return rez


def find_path(universe_coord1, universe_coord2) -> int:
    rez = abs(universe_coord1[0] - universe_coord2[0]) + abs(universe_coord1[1] - universe_coord2[1])
    return rez


def sum_path(matrix: list) -> int:

    universes_coord = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                universes_coord.append((i, j))
    rez = 0
    for universe_coord1 in universes_coord:
        for universe_coord2 in universes_coord:
            if universe_coord1 != universe_coord2:
                rez += find_path(universe_coord1, universe_coord2)
    return rez


def main():
    with open('input.txt', 'r') as f:
        matrix = [line.rstrip("\n") for line in f.readlines()]
    extend_m = extend_matrix(matrix)
    rez = sum_path(extend_m)/2
    print(rez)


if __name__ == "__main__":
    main()
