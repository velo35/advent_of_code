from collections import Counter

input_file = 1 and 'real.txt' or 'sample.txt'

with open('2021/day_14/input/' + input_file) as f:
    input = f.read()

lines = input.splitlines()

compound = lines[0]
patterns = {x: y for x, y in [line.split(' -> ') for line in lines[2:]]}

def next_compound(compound):
    next = []
    for i in range(len(compound) - 1):
        seq = compound[i:i+2]
        if seq in patterns:
            next.append((i+1, patterns[seq]))

    result = list(compound)
    for ndx, val in reversed(next):
        result.insert(ndx, val)
    return ''.join(result)

def task_1(compound):
    for i in range(10):
        compound = next_compound(compound)
    values = sorted(Counter(compound).values())
    print("task 1:", values[-1] - values[0])

def compound_counts(seq, steps, memoization):
    if (seq, steps) in memoization:
        return memoization[(seq, steps)]
    
    counts = dict()
    if steps > 0 and seq in patterns:
        val = patterns[seq]
        counts[val] = 1
        for a, b in compound_counts(seq[0] + val, steps - 1, memoization).items():
            counts[a] = b + counts.get(a, 0)
        for a, b in compound_counts(val + seq[1], steps - 1, memoization).items():
            counts[a] = b + counts.get(a, 0)

    memoization[(seq, steps)] = counts
    return counts

def task_2(compound):
    memoization = dict()
    counts_list = []
    steps = 40
    for i in range(len(compound) - 1):
        seq = compound[i:i+2]
        counts_list.append(compound_counts(seq, steps, memoization))
    
    counts_list.append(Counter(compound))
    result = dict()
    for counts in counts_list:
        for a, b in counts.items():
            result[a] = b + result.get(a, 0)

    values = sorted(result.values())
    print("task 2:", values[-1] - values[0])

task_1(compound)
task_2(compound)