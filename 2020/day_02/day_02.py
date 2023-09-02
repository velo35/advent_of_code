import collections

input_file = 1 and 'real.txt' or 'sample.txt'

with open('2020/day_02/input/' + input_file) as f:
    input = f.read()

def task_1(lines):
    valid = [1 for r, c, password in [([int(x) for x in r.split('-')], c[0], pw) for r, c, pw in [line.split(' ') for line in lines]] if collections.Counter(password)[c] in range(r[0], r[1] + 1)]
    print("task_1:", len(valid))

def task_2(lines):
    valid = [1 for a, b in [(c == password[r[0] - 1], c == password[r[1] - 1]) for r, c, password in [([int(x) for x in r.split('-')], c[0], pw) for r, c, pw in [line.split(' ') for line in lines]]] if a ^ b]
    print("task_2:", len(valid))

lines = input.splitlines()
task_1(lines)
task_2(lines)
