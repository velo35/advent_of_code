import os, re

def task_1(games):
    max = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    sum = 0

    for i, game in enumerate(games):
        valid = True
        
        for hand in game[game.index(':') + 1:].split(';'):
            values = [x.strip().split(' ') for x in hand.split(',')]
            counts = {c: int(n) for n, c in values}
            valid = valid and all(max[c] >= counts[c] for c in max if c in counts)
        if valid:
            sum += i + 1
        
    return sum

def task_2(games):
    sum = 0

    for i, game in enumerate(games):
        fewest = dict()

        for hand in game[game.index(':') + 1:].split(';'):
            values = [x.strip().split(' ') for x in hand.split(',')]
            
            counts = {c: int(n) for n, c in values}
            for c, n in counts.items():
                if c not in fewest or fewest[c] < n:
                    fewest[c] = n
        power = 1
        for n in fewest.values():
            power *= n
        sum += power
    return sum
        
                
        

if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and "sample.txt" or "real.txt"
    with open(os.path.join(os.path.dirname(__file__), input_filename)) as f:
        input = f.read()

    games = input.splitlines()
    print('task 1: ', task_1(games))
    print('task 2: ', task_2(games))
