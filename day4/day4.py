def get_match(line: str) -> list:
    numbers = line.split(":")[1].split("|")
    left = numbers[0].split()
    right = numbers[1].split()
    match_list = [i for i in left if i in right]
    return match_list


def main():
    with open('input.txt', 'r') as f:
        result = 0
        for line in f.readlines():
            line_ = line.rstrip("\n")
            match_list = get_match(line_)
            if match_list:
                print(match_list)
                result += pow(2, len(match_list) - 1)
    print(result)
    return result


if __name__ == "__main__":
    main()
