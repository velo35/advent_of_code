from collections import Counter

def task_1(group_declarations):
    print('task_1:', sum([len(Counter(''.join(group))) for group in group_declarations]))

def task_2(group_declarations):
    print('task_2:', sum([len([1 for k, v in Counter(''.join(group)).items() if v == len(group)]) for group in group_declarations]))

def process_input(use_sample):
    input_file = use_sample and 'sample.txt' or 'real.txt'
    with open('2020/day_06_CustomCustoms/input/' + input_file) as f:
        input = f.read()

    group_declarations = []
    group = []
    for line in input.splitlines():
        if not line:
            group_declarations.append(group)
            group = []
        else:
            group.append(line)    

    if group:
        group_declarations.append(group)
    return group_declarations

if __name__ == '__main__':
    group_declarations = process_input(use_sample = False)
    task_1(group_declarations)
    task_2(group_declarations)