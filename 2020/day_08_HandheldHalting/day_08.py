import os

def task_1(program):
    pc = 0
    acc = 0
    seen = set()

    while True:
        if pc in seen:
            break
        seen.add(pc)
        match program[pc][0]:
            case 'nop':
                pc += 1
            case 'acc':
                acc += program[pc][1]
                pc += 1
            case 'jmp':
                pc += program[pc][1]

    return acc

def task_2(program):
    nop_or_jmp = [(i, (ins, cnt)) for i, (ins, cnt) in enumerate(program) if ins in ('nop', 'jmp')]

    for i, (ins, cnt) in nop_or_jmp:
        new_program = [x for x in program]
        new_program[i] = ('nop' if ins == 'jmp' else 'jmp', cnt)
        pc = 0
        acc = 0
        seen = set()

        while True:
            if pc >= len(new_program):
                print('changed:', i, ins, cnt)
                return acc
            if pc in seen:
                break
            seen.add(pc)
            match new_program[pc][0]:
                case 'nop':
                    pc += 1
                case 'acc':
                    acc += new_program[pc][1]
                    pc += 1
                case 'jmp':
                    pc += new_program[pc][1]

    return None

if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), 'input', input_filename)) as f:
        input = f.read()

    program = [(ins, int(cnt)) for ins, cnt in [tuple(x.split(' ')) for x in input.splitlines()]]

    print('task 1: ', task_1(program))
    print('task 2: ', task_2(program))