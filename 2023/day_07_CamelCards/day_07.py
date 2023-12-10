import os
from collections import Counter

def hand_type(hand, jokerWild = False):
    cards = Counter(hand)

    if jokerWild and 'J' in cards:
        jokers = cards['J']
        del cards['J']
        if cards:
            first, *second = sorted(cards.values(), reverse=True)
            second = second[0] if second else None
            first += jokers
        else:
            first = jokers
    else:
        first, *second = sorted(cards.values(), reverse=True)
        second = second[0] if second else None

    match first:
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            return 4 if second == 2 else 3
        case 2:
            return 2 if second == 2 else 1

    return 0

def task_1(plays):
    table = str.maketrans("AKQJT", "EDCBA")
    order = sorted([(hand_type(hand), hand.translate(table), bid, hand) for hand, bid in plays])
    return sum([(i + 1) * bid for i, (_, _, bid, _) in enumerate(order)])

def task_2(plays):
    table = str.maketrans("AKQJT", "EDC1A")
    order = sorted([(hand_type(hand, True), hand.translate(table), bid, hand) for hand, bid in plays])
    return sum([(i + 1) * bid for i, (_, _, bid, _) in enumerate(order)])
    

if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), input_filename)) as f:
        input = f.read()

    plays = [(line.split()[0], int(line.split()[1])) for line in input.splitlines()]
    print('task 1:', task_1(plays))
    print('task 2:', task_2(plays))