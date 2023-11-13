import os
from collections import Counter

decode = {
    '#': '1',
    '.': '0'
}

def run_filter(algo, input_image, fill):
    df = decode[fill]
    w0 = len(input_image[0])
    input_image = [[df] * (w0 + 2)] + [[df] + [decode[x] for x in row] + [df] for row in input_image] + [[df] * (w0 + 2)]
    w, h = len(input_image[0]), len(input_image)
    output_image = [[None] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            lookup = ''.join([input_image[i + di][j + dj] if i + di in range(h) and j + dj in range(w) else df for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]])
            output_image[i][j] = algo[int(lookup, 2)]

    return output_image

def task_1(algo, image):
    output_image = run_filter(algo, run_filter(algo, image, fill='.'), fill=algo[0])
    return Counter(''.join([''.join(x) for x in output_image]))['#']

def task_2(algo, image):
    fill='.'

    for k in range(50):
        image = run_filter(algo, image, fill)
        fill = algo[0] if fill == '.' else algo[255]

    return Counter(''.join([''.join(x) for x in image]))['#']


if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    input_file = os.path.join(os.path.dirname(__file__), 'input', input_filename)
    with open(input_file) as f:
        input = f.read()

    lines = input.splitlines()
    div = lines.index('')
    algo = ''.join(lines[:div])
    image = [list(line) for line in lines[div+1:]]

    print('task_1: ', task_1(algo, image))
    print('task_2: ', task_2(algo, image))