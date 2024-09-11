from collections import Counter
from dataclasses import dataclass

RIGHT = 1
LEFT = 2
UP = 3
BOTTOM = 4


@dataclass(frozen=True)
class Beam:
    x: int
    y: int
    path: int

    _processed_cache = set()

    def get_nexts(self, matrix) -> list:
        if self in Beam._processed_cache:
            return []
        else:
            Beam._processed_cache.add(self)

        if self.path == RIGHT:
            x_next = self.x + 1
            y_next = self.y
        elif self.path == LEFT:
            x_next = self.x - 1
            y_next = self.y
        elif self.path == UP:
            x_next = self.x
            y_next = self.y - 1
        elif self.path == BOTTOM:
            x_next = self.x
            y_next = self.y + 1
        else:
            raise RuntimeError(f"unknown path {self.path}")
        if x_next < 0 or y_next < 0:
            return []
        try:
            next_symbol = matrix[y_next][x_next]
        except Exception:
            return []
        paths = []
        if next_symbol == '.':
            paths.append(self.path)
        if next_symbol == '-':
            if self.path in [RIGHT, LEFT]:
                paths.append(self.path)
            else:
                paths.extend([RIGHT, LEFT])
        if next_symbol == '|':
            if self.path in [UP, BOTTOM]:
                paths.append(self.path)
            else:
                paths.extend([UP, BOTTOM])
        if next_symbol == '/':
            if self.path == RIGHT:
                paths.append(UP)
            if self.path == LEFT:
                paths.append(BOTTOM)
            if self.path == UP:
                paths.append(RIGHT)
            if self.path == BOTTOM:
                paths.append(LEFT)
        if next_symbol == "\\":
            if self.path == RIGHT:
                paths.append(BOTTOM)
            if self.path == LEFT:
                paths.append(UP)
            if self.path == UP:
                paths.append(LEFT)
            if self.path == BOTTOM:
                paths.append(RIGHT)
        return [Beam(x_next, y_next, path) for path in paths]


def count_energized(all_data: list) -> int:
    result = 0
    for line in all_data:
        result += Counter(line)[1]
    return result


def find_path(data: list) -> list:
    new_data = []
    for line in data:
        pass
    return new_data


def print_field(m):
    print('\n'.join(''.join(str(e) for e in line) for line in m))


def main():

    with open('input.txt', 'r') as f:
        all_field = []
        for line in f.readlines():
            line_ = line.rstrip("\n")
            if line_:
                all_field.append(list(line_))

    size_x = len(all_field[0])
    size_y = len(all_field)
    empty_matrix = [["." for i in range(size_x)] for j in range(size_y)]

    start_beams = Beam(-1, 0, 1)
    beams = [start_beams]

    while beams:
        current = beams.pop()

        if current.x >= 0:
            empty_matrix[current.y][current.x] = 1
        beams.extend(current.get_nexts(all_field))

    result = count_energized(empty_matrix)
    print("result", result)
    return result


if __name__ == "__main__":
    main()
