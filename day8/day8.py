def get_results(dict_input: dict, rules_input: str) -> int:
    current_elem = 'AAA'
    index = 0
    result = 0
    while current_elem != "ZZZ":
        if rules_input[index] == "R":
            current_elem = dict_input[current_elem][1]
        if rules_input[index] == "L":
            current_elem = dict_input[current_elem][0]
        index += 1
        index %= len(rules_input)
        result += 1
    return result


def main():
    map_dict = {}
    with open('input.txt', 'r') as f:
        rules = f.readline().rstrip("\n")
        for line in f.readlines()[1:]:
            line_ = line.rstrip("\n")
            line_str = line_.split("=")
            map_key = line_str[0].strip()
            map_value = line_str[1].strip()[1:-1].split(",")
            map_dict[map_key] = [i.strip() for i in map_value]

    result = get_results(map_dict, rules)
    print(result)
    return 0


if __name__ == "__main__":
    main()
