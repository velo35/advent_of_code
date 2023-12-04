import os, re

def task_1(cards):
    score = 0
    for card in cards:
        winning = {int(x) for x in re.findall("\d+", card[card.index(':'): card.index('|')])}
        mine = {int(x) for x in re.findall("\d+", card[card.index('|'):])}
        count = len(winning & mine)
        score += 2 ** (count - 1) if count > 0 else 0

    return score

def task_2(cards):
    wins = [0] * len(cards)
    for i, card in enumerate(cards):
        winning = {int(x) for x in re.findall("\d+", card[card.index(':'): card.index('|')])}
        mine = {int(x) for x in re.findall("\d+", card[card.index('|'):])}
        wins[i] = len(winning & mine)

    # results = [[i + 1] for i in range(len(cards))]
    # for i in reversed(range(len(cards))):
    #     for j in range(i + 1, i + 1 + wins[i]):
    #         results[i] += results[j]
    # print(Counter(x for list in results for x in list))
    # return sum(x for x in Counter(x for list in results for x in list).values())

    counts = [1] * range(len(cards))
    sum = 0
    for i in reversed(range(len(cards))):
        for j in range(i + 1, i + 1 + wins[i]):
            counts[i] += counts[j]
        sum += counts[i]

    return sum

if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), input_filename)) as f:
        input = f.read()

    cards = input.splitlines()
    print("task 1:", task_1(cards))
    print("task 2:", task_2(cards))