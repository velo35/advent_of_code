input_file = 1 and 'real.txt' or 'sample.txt'

with open('2021/day_13/input/' + input_file) as f:
    input = f.read()

lines = input.split('\n')
points_delimeter = lines.index('')

points = {tuple([int(x) for x in line.split(',')]) for line in lines[:points_delimeter]}
commands = [(line[11], int(line[13:])) for line in lines[points_delimeter + 1:]]

def fold(points, command):
    axis, v = command
    if axis == 'y':
        return {(x, v - (y - v) if y > v else y) for (x, y) in points}
    else:
        return {(v - (x - v) if x > v else x, y) for (x, y) in points}

def task_1():
    print('task 1:', len(fold(points, commands[0])))

def task_2(points):
    for command in commands:
        points = fold(points, command)
    maxX = max([x for x, y in points]) + 1
    maxY = max([y for x, y in points]) + 1
    grid = [['.'] * maxX for _ in range(maxY)]
    for x, y in points:
        grid[y][x] = '#'
    print('task 2:')
    print(''.join([''.join(x) + '\n' for x in grid]))

#task_1()
task_2(points)