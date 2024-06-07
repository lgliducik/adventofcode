from dataclasses import dataclass


@dataclass
class Round:
    green: int
    blue: int
    red: int

    def __init__(self, green, blue, red):
        self.green = green
        self.blue = blue
        self.red = red

    def possible(self) -> bool:
        if self.red <= 12 and self.green <= 13 and self.blue <= 14:
            return True
        else:
            return False


@dataclass
class Game:
    number: int
    rounds: list

    def __init__(self, number, rounds):
        self.number = number
        self.rounds = rounds

    def possible(self) -> bool:
        return all(i.possible() for i in self.rounds)


def parse_round(str_round) -> Round:
        number_color_list = str_round.split(",")
        round = Round(0, 0, 0)
        for number_color in number_color_list:
            number_color = number_color.strip()
            str_num, color = number_color.split(" ")
            setattr(round, color, int(str_num))
        return round


def parse_line(line_input) -> Game:
    game_id = int(line_input.split(":")[0].split()[1])
    str_rounds = line_input.split(":")[1].split(";")
    rounds = [parse_round(r) for r in str_rounds]
    game = Game(game_id, rounds)
    return game


def main():
    with open('input.txt', 'r') as f:
        result = 0
        for line in f.readlines():
            line_ = line.rstrip("\n")
            game = parse_line(line_)
            if game.possible():
                result += game.number
    print(result)
    return result


if __name__ == "__main__":
    main()
