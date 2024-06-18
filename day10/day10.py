from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def check(self, matrix: list, cases: str):
        return matrix[self.y][self.x] in cases


def get_next(matrix: list, point: Point, prev_point: Point = None) -> Point:
    for new_point, correct_next_points, correct_current_points in [
        (Point(point.x, point.y + 1), "|LJS", "|7F"),  # bottom
        (Point(point.x, point.y - 1), "|7FS", "|LJ"),  # upper
        (Point(point.x + 1, point.y), "-J7S", "-FL"),  # right
        (Point(point.x - 1, point.y), "-FLS", "-7J"),  # left
    ]:
        if prev_point is not None:
            if new_point == prev_point or not point.check(matrix, correct_current_points):
                continue
        if matrix[new_point.y][new_point.x] in correct_next_points:
            return new_point
    raise RuntimeError(f"there is no next point {point}")


def task(matrix: list, start_point: Point) -> int:
    index = 0
    point = get_next(matrix, start_point)
    prev = start_point
    while point != start_point:
        next_point = get_next(matrix, point, prev)
        symbol = matrix[next_point.y][next_point.x]
        print(f"{next_point} {symbol}")
        prev = point
        point = next_point
        index += 1
    return index//2 + 1


def fins_s(matrix: list) -> Point:
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "S":
                return Point(x, y)


def main():
    with open('input.txt', 'r') as f:
        matrix = [line.rstrip("\n") for line in f.readlines()]

    print(matrix)
    point_start = fins_s(matrix)
    print(point_start, matrix[point_start.y][point_start.x])
    result = task(matrix, point_start)
    print(result)


if __name__ == "__main__":
    main()
