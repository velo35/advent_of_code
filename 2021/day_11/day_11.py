input_file = 1 and 'real.txt' or 'sample.txt'

with open('2021/day_11/input/' + input_file) as f:
    input = f.read()

grid = [[int(x) for x in line] for line in input.split('\n')]
size = 10
neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def step(grid):
    new_flashing = set()
    for i in range(size):
        for j in range(size):
            grid[i][j] += 1
            if grid[i][j] > 9:
                new_flashing.add((i, j))

    flashing = set()            
    while new_flashing:
        flashing |= new_flashing
        next_flashing = set()
        for (i, j) in new_flashing:
            for (v, h) in neighbors:
                if i + v >= 0 and i + v < size and j + h >= 0 and j + h < size:
                    grid[i + v][j + h] += 1
                    if grid[i + v][j + h] > 9 and (i + v, j + h) not in flashing:
                        next_flashing.add((i + v, j + h))
        new_flashing = next_flashing
    
    for (i, j) in flashing:
        grid[i][j] = 0

    return len(flashing)

def task_1(grid, steps):
    flashes = 0

    for _ in range(steps):
        flashes += step(grid)

    print('task 1:', flashes)
    
def task_2(grid):
    steps = 0
    while True:
        steps += 1
        if size * size == step(grid):
            break
    print('task 2:', steps)


task_1([x.copy() for x in grid], 100)
task_2([x.copy() for x in grid])