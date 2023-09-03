input_file = 1 and 'real.txt' or 'sample.txt'

with open('2020/day_03/input/' + input_file) as f:
    input = f.read()

def task_1(grid):
    grid_width = len(grid[0])
    tree_count = 0

    for i in range(len(grid)):
        j = (3 * i) % grid_width
        if grid[i][j] == '#':
            tree_count += 1

    print('task_1:', tree_count)

def task_2(grid):
    grid_width = len(grid[0])
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts = []

    for dx, dy in slopes:
        tree_count = 0
        j = 0
        for i in range(0, len(grid), dy):
            if grid[i][j] == '#':
                tree_count += 1
            j = (j + dx) % grid_width
        tree_counts.append(tree_count)
    result, *rest = tree_counts
    for v in rest:
        result *= v
    print(result)

grid = input.splitlines()
task_1(grid)
task_2(grid)