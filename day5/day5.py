from dataclasses import dataclass


@dataclass
class Interval:
    dest_start: int
    source_start: int
    range: int

    def convert_number(self, number) -> int:
        return self.dest_start + (number - self.source_start)

    def number_in_interval(self, number) -> bool:
        return (number > self.dest_start) and (number < self.source_start + self.range)


@dataclass
class Convert:
    destination: str
    source: str
    list_of_interval: list

    def convert(self, number):
        for interval in self.list_of_interval:
            if interval.number_in_interval(number):
                return interval.convert_number(number)
        return number

    def __str__(self):
        intervals = "".join(f"{i.dest_start},{i.source_start},{i.range}\n" for i in self.list_of_interval)
        return f"destination: {self.destination}\nsource: {self.source}\n list of intervals\n {intervals}"


def line_to_interval(line: str) -> Interval:
    source_start, dest_start, rang = line.split()
    interval = Interval(int(source_start), int(dest_start), int(rang))
    return interval


def block_to_convert(block: str) -> Convert:
    convert = Convert(0, 0, [])
    lines = [i for i in block.split("\n")]
    for line_ in lines:
        if "map:" in line_:
            converter_str = line_.split()[0]
            source = converter_str.split("-")[0]
            dest = converter_str.split("-")[2]
            convert.source = source
            convert.destination = dest
        else:
            interval = line_to_interval(line_)
            convert.list_of_interval.append(interval)
    print(convert)
    return convert


def main():
    result_list_location = []
    with open('input.txt', 'r') as f:
        all_file = f.read()
        blocks = all_file.split("\n\n")
        seeds_str = blocks[0].rstrip("\n").split(":")[1].split()
        seeds = [int(i) for i in seeds_str]
        print(seeds)

        for block in blocks[1:]:
            print(block)
            convert_list = []
            convert_list.append(block_to_convert(block))

        for seed in seeds:
            seed_start = seed
            for convert in convert_list:
                seed_start = convert.convert(seed_start)
            result_list_location.append(seed_start)
        print(min(result_list_location))
        return min(result_list_location)


if __name__ == "__main__":
    main()

