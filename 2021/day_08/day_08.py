input_file = 1 and "real.txt" or "sample.txt"

with open("2021/day_8/input/" + input_file) as f:
    input = f.read()

lines = [(x, y) for x, y in [line.split('|') for line in input.split('\n')]]

def task_1():
    count = 0
    for input, output in lines:
        for digit in output.strip().split(' '):
            digitLen = len(digit)
            if digitLen in [2, 4, 3, 7]:
                count += 1
        
    print("task 1:", count)

def decode(input, output):
    digits = input.strip().split(' ')
    digits.sort(key = lambda x: len(x))
    decoder = dict()

    seven = frozenset(digits[1])
    four = frozenset(digits[2])
    decoder[frozenset(digits[0])] = "1"
    decoder[seven] = "7"
    decoder[four] = "4"
    decoder[frozenset(digits[-1])] = "8"

    fives = [frozenset(x) for x in digits[3:6]]
    for x in fives:
        if len(x - seven) == 2:
            three = x
    decoder[three] = "3"
    fives = [x for x in fives if x != three]

    for x in fives:
        if len(x - four) == 2:
            five = x
    decoder[five] = "5"
    fives = [x for x in fives if x != five]

    decoder[fives[0]] = "2"

    sixes = [frozenset(x) for x in digits[6:9]]
    for x in sixes:
        if len(x - three) == 1:
            nine = x
    decoder[nine] = "9"
    sixes = [x for x in sixes if x != nine]

    for x in sixes:
        if len(x - five) == 1:
            six = x
    decoder[six] = "6"
    sixes = [x for x in sixes if x != six]

    decoder[sixes[0]] = "0"

    return int("".join([decoder[frozenset(x)] for x in output.strip().split(' ')]))

def task_2():
    print("task 2:", sum([decode(input, output) for input, output in lines]))

        

task_1()
task_2()