from dataclasses import dataclass
import functools


@dataclass
class Race:
    time: int
    distance: int

    def number_of_win(self) -> int:
        number = 0
        for i in range(self.time)[1:-1]:
            if (self.time - i) * i > self.distance:
                number += 1
        return number


def main():
    with open('input.txt', 'r') as f:
        result = []
        line1 = f.readline()
        line1 = line1.rstrip("\n")
        print(line1)
        times = line1.split(":")[1].split()

        line2 = f.readline()
        line2 = line2.rstrip("\n")
        print(line2)
        distances = line2.split(":")[1].split()

        list_race = []
        for j in range(len(times)):
            race = Race(int(times[j]), int(distances[j]))
            list_race.append(race)
        result = [i.number_of_win() for i in list_race]

    result_number = functools.reduce(lambda a, b: a * b, result)
    print(result_number)
    return result_number


if __name__ == "__main__":
    main()
