import numpy as np


def is_mirror(matrix: np.matrix, index: int) -> bool:
    index_1 = index
    index_2 = index + 1
    while index_1 >= 0 and index_2 < len(matrix):
        if np.all(matrix[index_1] == matrix[index_2]):
            index_1 -= 1
            index_2 += 1
        else:
            return False
    return True


def find_mirror(matrix: np.matrix) -> int:
    left_vert = 0
    row_up = 0

    index = 0
    while index < matrix.shape[0] - 1:
        if is_mirror(matrix, index):
            row_up = index+1
            print(f"row_up = {row_up}")
            return 100 * row_up
        index += 1
    index = 0
    while index < matrix.shape[1] - 1:
        if is_mirror(np.transpose(matrix), index):
            left_vert = index + 1
            print(f"left_vert = {left_vert}")
            return left_vert
        index += 1

    raise RuntimeError()


def main():
    with open('input.txt', 'r') as f:
        result = 0
        new_field = []
        all_field = []
        for line in f.readlines():
            line_ = line.rstrip("\n")
            print(f"{line_}")
            if line_:
                new_field.append(list(line_))
            else:
                matrix = np.matrix(new_field)
                all_field.append(matrix)
                new_field = []
        if new_field:
            matrix = np.matrix(new_field)
            all_field.append(matrix)

    print(all_field)

    number = 0
    for matr in all_field:
        result += find_mirror(matr)
        print(f"number = {number}\n")
        number += 1

    print(result)
    return result


if __name__ == "__main__":
    main()