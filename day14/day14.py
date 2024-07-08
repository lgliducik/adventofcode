import numpy as np


def should_go_up(matrix, y, x) -> bool:
    return y >= 0 and matrix[y][x] not in '#O'


def up_circle(matrix: np.array, y: int, x: int) -> np.array:
    y_next = y - 1
    while should_go_up(matrix, y_next, x):
        y_next -= 1

    if y_next + 1 != y:
        matrix[y_next + 1, x] = 'O'
        matrix[y, x] = '.'
    return matrix


def moving_circle(matrix: np.matrix) -> np.matrix:

    for y in range(1, matrix.shape[0]):
        for x in range(matrix.shape[1]):
            if matrix[y, x] == 'O':
                matrix = up_circle(matrix, y, x)

    return matrix


def find_count(line) -> int:
    return len(list(filter(lambda x: x == 'O', line)))


def main():
    with open('input.txt', 'r') as f:
        result = 0
        new_field = []
        for line in f.readlines():
            new_field.append(list(line.rstrip("\n")))

    matrix = np.array(new_field)

    new_matrix = moving_circle(matrix)

    for index, item in zip(range(len(new_matrix), 0, -1), new_matrix):
        result += index * find_count(item)

    print(result)
    return result


if __name__ == "__main__":
    main()
