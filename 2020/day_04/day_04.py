import string

input_file = 1 and 'real.txt' or 'sample.txt'

with open('2020/day_04/input/' + input_file) as f:
    input = f.read()

def task_1(infos):
    required_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    valid = [info for info in infos if set(info.keys()) >= required_keys]
    print('task_1:', len(valid))

def task_2(infos):
    required_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    candidate_infos = [info for info in infos if set(info.keys()) >= required_keys]

    field_is_valid = {
        'byr': lambda x: x.isdigit() and int(x) in range(1920, 2003),
        'iyr': lambda x: x.isdigit() and int(x) in range(2010, 2021),
        'eyr': lambda x: x.isdigit() and int(x) in range(2020, 2031),
        'hgt': lambda x: x[:-2].isdigit() and int(x[:-2]) in range(150, 194) if 'cm' == x[-2:] else 'in' == x[-2:] and x[:-2].isdigit() and int(x[:-2]) in range(59, 77),
        'hcl': lambda x: x[0] == '#' and all(c in string.hexdigits for c in x[1:]),
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: x.isdigit() and len(x) == 9,
        'cid': lambda x: True
    }

    valid_infos = [info for info in candidate_infos if all(field_is_valid[k](v) for k, v in info.items())]
    print('task_2:', len(valid_infos))

kv_lines = [[tuple(kv.split(':')) for kv in line.split()] for line in input.splitlines()]
infos = []
info = dict()

for kv_line in kv_lines:
    if not kv_line:
        infos.append(info)
        info = dict()
    else:
        d = dict(kv_line)
        info.update(d)
if len(info) > 0:
    infos.append(info)

task_1(infos)
task_2(infos)