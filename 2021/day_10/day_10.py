input_file = 1 and 'real.txt' or 'sample.txt'

with open('2021/day_10/input/' + input_file) as f:
    input = f.read()

lines = input.split('\n')

def push(x, stack):
    stack.append(x)
    return True

pairs = {
    '(' : ')',
    '{' : '}',
    '<' : '>',
    '[' : ']',
}

points_1 = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

def check_pop(x, stack):
    if len(stack) > 0 and x == pairs[stack[-1]]:
        stack.pop()
        return True
    return False

action = {
    '(' : push,
    ')' : check_pop,
    '{' : push,
    '}' : check_pop,
    '<' : push,
    '>' : check_pop,
    '[' : push,
    ']' : check_pop
}

def task_1():
    score = 0
    for line in lines:
        stack = []
        for x in line:
            if not action[x](x, stack):
                score += points_1[x]
                break

    print("task_1:", score)

points_2 = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

def task_2():
    scores = []
    for line in lines:
        stack = []
        incomplete = True
        for x in line:
            if not action[x](x, stack):
                incomplete = False
                break
        if incomplete:
            completion = ""
            score = 0
            while stack:
                v = pairs[stack.pop()]
                score = score * 5 + points_2[v]
                completion += v
            scores.append(score)
    print("task_2:", sorted(scores)[len(scores) // 2])

task_1()
task_2()