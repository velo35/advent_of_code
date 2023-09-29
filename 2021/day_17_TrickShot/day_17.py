import math, re

def task_1(x0, x1, y0, y1):
    n = abs(y1) - 1
    return n * (n + 1) // 2

def task_2(x0, x1, y0, y1):
    vx_min = int((math.sqrt(1 + 8 * x0) - 1) / 2)
    vx_max = x1 + 1
    vy_min = y1
    vy_max = abs(y1)

    res = []
    for ivx in range(vx_min, vx_max):
        for ivy in range(vy_min, vy_max):
            vx = ivx
            vy = ivy
            px = py = 0
            
            while px <= x1 and py >= y1:
                if px in range(x0, x1 + 1) and py in range(y0, y1 - 1, -1):
                    res.append((ivx, ivy))
                    break
                px += vx
                vx = max(vx - 1, 0)
                py += vy
                vy -= 1

    return len(res)


if __name__ == '__main__':
    use_sample = False
    input_file = use_sample and 'sample.txt' or 'real.txt'
    with open('2021/day_17_TrickShot/input/' + input_file) as f:
        input = f.read()

    x0, x1, y1, y0 = [int(x) for x in re.findall('-?\d+', input)]

    print('task_1: ', task_1(x0, x1, y0, y1))
    print('task_2: ', task_2(x0, x1, y0, y1))