def collect_number(matrix: list, x: int, y: int) -> tuple[int, int]:
    found_number_str = ''
    while matrix[y][x].isdigit():
        found_number_str += matrix[y][x]
        x += 1
        if x >= len(matrix[0]):
            break
    return x - 1, int(found_number_str)


def safe_is_symbol(matrix: list, x: int, y: int) -> bool:
    if y < 0 or y >= len(matrix):
        return False
    if x < 0 or x >= len(matrix[0]):
        return False
    return matrix[y][x] != "."


def is_part(matrix: list, x_start: int, x_end: int, y: int) -> bool:
    for i in range(x_start - 1, x_end + 2):
        if safe_is_symbol(matrix, i, y - 1):
            return True

    for i in range(x_start - 1, x_end + 2):
        if safe_is_symbol(matrix, i, y + 1):
            return True

    if safe_is_symbol(matrix, x_start-1, y):
        return True
    if safe_is_symbol(matrix, x_end + 1, y):
        return True
    return False


def task1(matrix: list) -> int:
    result = 0
    x = 0
    y = 0

    while y < len(matrix):
        if matrix[y][x].isdigit():
            end_number_x, number = collect_number(matrix, x, y)
            if is_part(matrix, x, end_number_x, y):
                result += number
                print(number)
            x = end_number_x
        x += 1
        if x >= len(matrix[0]):
            x = 0
            y += 1
    return result


def main():
    with open('input.txt', 'r') as f:
        matrix = [l.rstrip("\n") for l in f.readlines()]
        result = task1(matrix)

    print(result)


if __name__ == "__main__":
    main()
