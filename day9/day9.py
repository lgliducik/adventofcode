def get_result(lists: list) -> int:
    res = 0
    for i in reversed(range(len(lists))):
        res += lists[i][-1]
    return res


def get_dif(lst: list) -> int:
    start_lst = lst
    result_lst = [start_lst]
    while not all([i == 0 for i in start_lst]):
        new_lst = []
        for i in range(len(start_lst) - 1):
            new_lst.append(start_lst[i+1] - start_lst[i])

        if not all([i == 0 for i in start_lst]):
            result_lst.append(new_lst)
        start_lst = new_lst
    rez = get_result(result_lst)
    return rez


def main():
    with open('input.txt', 'r') as f:
        result = 0
        for line in f.readlines():
            line_ = line.rstrip("\n")
            list_numbers = list(map(int, line_.split()))
            result += get_dif(list_numbers)
    return result


if __name__ == "__main__":
    main()
