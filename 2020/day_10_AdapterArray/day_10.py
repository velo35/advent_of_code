import os

def task_1(adapters):
    three = 0
    one = 0
    adapters = sorted([0] + adapters)
    for i, a in enumerate(adapters):
        if i > 0:
            if a - adapters[i - 1] == 1:
                one += 1
            if a - adapters[i - 1] == 3:
                three += 1

    return one * (three + 1)

def task_2(adapters):
    adapters = sorted([0] + adapters, reverse=True)
    counts = {adapters[0]: 1}

    for i in range(1, len(adapters)):
        count = 0
        if i - 3 >= 0 and adapters[i - 3] - adapters[i] <= 3:
            count += counts[adapters[i - 3]]
        if i - 2 >= 0 and adapters[i - 2] - adapters[i] <= 3:
            count += counts[adapters[i - 2]]
        if i - 1 >= 0 and adapters[i - 1] - adapters[i] <= 3:
            count += counts[adapters[i - 1]]
        counts[adapters[i]] = count
    
    return counts[0]

if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), input_filename)) as f:
        input = f.read()

    adapters = [int(x) for x in input.splitlines()]
    print('task 1:', task_1(adapters))
    print('task 2:', task_2(adapters))
    