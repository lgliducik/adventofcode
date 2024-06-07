
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# 12, 38, 15, 77


def get_number(line_input):
    start_number = next(iter(c for c in line_input if str.isnumeric(c)))
    end_number = next(iter(c for c in reversed(line_input) if str.isnumeric(c)))
    return int(f"{start_number}{end_number}")


# def get_number(line_input):
#     start_number = None
#     end_number = None
#     start = 0
#     end = len(line_input)-1
#     while start <= end:
#         temp_start = line_input[start]
#         if str.isnumeric(temp_start) and start_number is None:
#             start_number = int(temp_start)
#
#         start += 1
#
#         temp_end = line_input[end]
#         if str.isnumeric(temp_end) and end_number is None:
#             end_number = int(temp_end)
#
#         end -= 1
#     if start_number and not end_number:
#         end_number = start_number
#
#     if end_number and not start_number:
#         start_number = end_number
#
#     return int(str(start_number) + str(end_number))


def main():
    with open('input.txt', 'r') as f:
        result = 0
        for line in f.readlines():
            line_ = line.rstrip("\n")
            if line_:

                res_line = get_number(line_)
                print(line_)
                print(res_line)
                result += res_line

    print(result)


if __name__ == "__main__":
    main()


