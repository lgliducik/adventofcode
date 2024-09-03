
def get_result(current_result: int, symbol: str) -> int:
    result = current_result
    result += ord(symbol)
    result = result * 17
    result = result % 256
    return result


def main():
    with open('input.txt', 'r') as f:
        new_field = []
        for line in f.read().strip('\n').split(','):
            new_field.append(line)

    result = 0
    for item in new_field:
        result_item = 0
        for symb in item:
            result_item = get_result(result_item, symb)
        result += result_item
    print(result)
    return result


if __name__ == "__main__":
    main()
