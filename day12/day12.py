from dataclasses import dataclass, replace


@dataclass
class Spring:
    spring_states: str
    notes: list


def check(spring: Spring) -> bool:
    return [len(i) for i in spring.spring_states.split(".") if i != ''] == spring.notes


def get_arrangements(spring: Spring) -> int:
    index = spring.spring_states.find("?")

    if index >= 0:
        spring_copy_point = replace(spring)
        spring_copy_cross = replace(spring)
        spring_copy_point.spring_states = spring_copy_point.spring_states.replace(spring_copy_point.spring_states[index], '.', 1)
        spring_copy_cross.spring_states = spring_copy_cross.spring_states.replace(spring_copy_cross.spring_states[index], '#', 1)
        return get_arrangements(spring_copy_point) + get_arrangements(spring_copy_cross)
    else:
        res = check(spring)
        if res:
            return 1
        else:
            return 0


def main():
    with open('input.txt', 'r') as f:
        springs = []
        result = 0
        for line in f.readlines():
            line_ = line.rstrip("\n")
            spring_states, notes_str = line_.split(" ")
            notes = list(map(lambda i: int(i), notes_str.split(",")))
            spring = Spring(spring_states, notes)
            springs.append(spring)
        print(springs)
        for spring in springs:
            result += get_arrangements(spring)
    print(result)
    return result


if __name__ == "__main__":
    main()