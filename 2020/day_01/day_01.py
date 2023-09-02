import bisect
import itertools

input_file = 1 and 'real.txt' or 'sample.txt'

with open('2020/day_01/input/' + input_file) as f:
    input = f.read()

def task_1(report):
    for i in range(bisect.bisect_right(report, 1010)):
        val = 2020 - report[i]
        j = bisect.bisect_left(report, val)
        if j != len(report) and report[j] == val:
            print("task_1:", report[i], report[j], report[i] * report[j])
            break

def task_2(report):
    i, j, k = [(i, j, k) for i, j, k in itertools.product(range(len(report)), repeat=3) if i < j and j < k and report[i] + report[j] + report[k] == 2020][0]
    print("task_2:", report[i], report[j], report[k], report[i] * report[j] * report[k])

report = sorted([int(x) for x in input.splitlines()])
task_1(report)
task_2(report)
