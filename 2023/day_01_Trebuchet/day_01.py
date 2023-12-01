import os, re

def task_1(lines):
    nums = []
    for line in lines:
        digits = re.findall(r"\d", line)
        nums.append(int(digits[0] + digits[-1]))
        
    return sum(nums)

def task_2(lines):
    nums = []
    values = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    for line in lines:
        digits = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line)
        digits = [values[x] if x in values else int(x) for x in digits]
        nums.append(10*digits[0] + digits[-1])

    return sum(nums)

if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample_2.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), input_filename)) as f:
        input = f.read()

    lines = input.splitlines()
    print('task 1:', task_1(lines))
    print('task 2:', task_2(lines))