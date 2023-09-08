def task_1(numeric_boarding_passes):
    print('task_1:', max(numeric_boarding_passes))

def task_2(numeric_boarding_passes):
    smallest = min(numeric_boarding_passes)
    largest = max(numeric_boarding_passes)
    total = sum(numeric_boarding_passes)
    print('task_2:', (1 + len(numeric_boarding_passes)) * (smallest + largest) // 2 - total)

def process_input(use_sample):
    input_file = use_sample and 'sample.txt' or 'real.txt'

    with open('2020/day_05_BinaryBoarding/input/' + input_file) as f:
        input = f.read()

    boarding_passes = input.splitlines()

    xfm = {
        ord('F'): '0', 
        ord('B'): '1',
        ord('L'): '0', 
        ord('R'): '1'
    }

    return [int(bp.translate(xfm), 2) for bp in boarding_passes]
    
if __name__ == '__main__':
    numeric_boarding_passes = process_input(use_sample = False)
    task_1(numeric_boarding_passes)
    task_2(numeric_boarding_passes)
