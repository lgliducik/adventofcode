from dataclasses import dataclass
import collections

@dataclass
class Hand:
    set_of_cards: str
    bid: int

    def get_power(self) -> float:
        counter = collections.Counter(self.set_of_cards)
        count = len(counter)
        if count == 1:
            return 5
        if count == 2:
            if max(counter.values()) == 4:
                return 4
            else:
                # full house
                return 3.5
        if count == 3:
            if max(counter.values()) == 3:
                return 3
            else:
                return 2
        if max(counter.values()) == 2:
            return 1
        if count == 5:
            # high card
            return 0.5
        raise RuntimeError(f"unknown rank {self.set_of_cards}")


def sort_key(hand: Hand):
    return hand.get_power(), hand.set_of_cards.translate(str.maketrans({"K": "X", "A": "Y", "T": "B"}))


def main():
    with open('input.txt', 'r') as f:
        hands = []
        for line in f.readlines():
            line_ = line.rstrip("\n")
            set_of_cards, bid = line_.split()
            hand = Hand(set_of_cards, int(bid))
            hands.append(hand)
        print(hands)

        hands_sorted = sorted(hands, key=sort_key)

        print(hands_sorted)
        result = sum((hand.bid * index) for index, hand in enumerate(hands_sorted, start=1))
        print(result)
    return result


if __name__ == "__main__":
    main()
