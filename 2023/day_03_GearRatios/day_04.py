import os, re, itertools

def task_1(layout):
    width = layout.index('\n')
    layout = ''.join(layout.split('\n'))
    s_indices = {match.span()[0] for match in re.finditer("[^.\d]", layout)}

    numbers = []
    for match in re.finditer("\d+", layout):
        f, l = match.span()
        left = f - 1 if f % width > 0 else f
        right = l - 1 if l % width == 0 else l
        
        if [1 for y in itertools.chain.from_iterable(range(left + x, right + x + 1) for x in [-width, 0, width]) if y in s_indices]:
            numbers.append(int(match[0]))
    
    return sum(numbers)

def task_2(layout):
    width = layout.index('\n')
    layout = ''.join(layout.split('\n'))
    indices = {match.span()[0]: [] for match in re.finditer("[*]", layout)}

    for match in re.finditer("\d+", layout):
        f, l = match.span()
        left = f - 1 if f % width > 0 else f
        right = l - 1 if l % width == 0 else l
        
        for g in [y for y in itertools.chain.from_iterable(range(left + x, right + x + 1) for x in [-width, 0, width]) if y in indices]:
            indices[g].append(int(match[0]))

    return sum([l[0] * l[1] for g, l in indices.items() if len(l) == 2])
    

if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), input_filename)) as f:
        input = f.read()

    print("task 1:", task_1(input))
    print("task 2:", task_2(input))