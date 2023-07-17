from collections import defaultdict

input_file = 'real.txt'

with open('2021/day_12/input/' + input_file) as f:
    input = f.read()

cave = defaultdict(set)
for line in input.split('\n'):
    a, b = line.split('-')
    if b != 'start':
        cave[a].add(b)
    if a != 'start':
        cave[b].add(a)

del cave['end']

def find_path_count(cave, current, visited, another_small):
    count = 0

    for next in cave[current]:
        if next == 'end':
            count += 1
        elif not next.islower() or next not in visited or another_small:
            next_another_small = another_small
            if next.islower() and next in visited:
                next_another_small = False
            count += find_path_count(cave, next, visited | {current}, next_another_small)
    return count

def task_1(cave):
    print('task 1:', find_path_count(cave, 'start', set(), False))

def task_2(cave):
    print('task 2:', find_path_count(cave, 'start', set(), True))

task_1(cave)
task_2(cave)