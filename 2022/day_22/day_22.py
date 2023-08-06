import re
from collections import namedtuple
from enum import IntEnum

Boundary = namedtuple('Boundary', 'first last')

class Direction(IntEnum):
    Right = 0
    Down = 1
    Left = 2
    Up = 3

    def isRight(self):
        return self == Direction.Right
    
    def isDown(self):
        return self == Direction.Down
    
    def isLeft(self):
        return self == Direction.Left
    
    def isUp(self):
        return self == Direction.Down
    
    def turn(self, amt):
        return [Direction.Right, Direction.Down, Direction.Left, Direction.Up][(self.value + amt) % 4]

    def step_amount(self):
        return 1 if self in [Direction.Right, Direction.Down] else -1

class Turn(IntEnum):
    Right = 1
    Left = -1

use_sample = 1
input_file = 'sample.txt' if use_sample else 'real.txt'

with open('2022/day_22/input/' + input_file) as f:
    input = f.read().splitlines()

map = input[:-2]
commands = [int(x) if x not in 'LR' else x for x in re.findall('(\d+|L|R)', input[-1])]

max_len = max([len(line) for line in map])
map = [line + ' ' * (max_len - len(line)) for line in map] # need to do this for v_edges
h_edges = [Boundary(f, l - 1) for f, l in [re.search('\S+', line).span() for line in map]]
v_edges = [Boundary(f, l - 1) for f, l in [re.search('\S+', line).span() for line in [''.join(x) for x in zip(*map)]]]
dir_change = {'L': Turn.Left, 'R': Turn.Right}

def task_1():
    x, y = h_edges[0][0], 0
    dir = Direction.Right

    for ins in commands:
        if isinstance(ins, int):
            match dir:
                case Direction.Right | Direction.Left:
                    for _ in range(ins):
                        next_x = x + dir.step_amount()
                        if x == h_edges[y].first and dir == Direction.Left: next_x = h_edges[y].last
                        if x == h_edges[y].last and dir == Direction.Right: next_x = h_edges[y].first
                        if map[y][next_x] == '#':
                            break
                        x = next_x
                case Direction.Down | Direction.Up:
                    for _ in range(ins):
                        next_y = y + dir.step_amount()
                        if y == v_edges[x].first and dir == Direction.Up: next_y = v_edges[x].last
                        if y == v_edges[x].last and dir == Direction.Down: next_y = v_edges[x].first
                        if map[next_y][x] == '#':
                            break
                        y = next_y
        else:
            dir = dir.turn(dir_change[ins])

    print('task 1:', 1000 * (y + 1) + 4 * (x + 1) + dir)

def next_step_sample(x, y, dir):
    size = 4
    s0 = 0
    s1 = size
    s2 = 2 * size
    s3 = 3 * size
    s4 = 4 * size

    # 1 - left edge
    if x == s2 and y in range(s0, s1) and dir.isLeft():
        print('1 - left edge')
        return s1 + y, s1, Direction.Down
    # 1 - top edge
    elif x in range(s2, s3) and y == 0 and dir.isUp():
        print('1 - top edge')
        return s1 - 1 - (x % size), s1, Direction.Down
    # 1 - right edge
    elif x == s3 - 1 and y in range(s0, s1) and dir.isRight():
        print('1 - right edge')
        return s4 - 1, s3 - 1 - y, Direction.Left
    # 2 - left edge
    elif x == 0 and y in range(s1, s2) and dir.isLeft():
        print('2 - left edge')
        return s4 - 1 - (y % size), s2 - 1, Direction.Up
    # 2 - top edge
    elif x in range(s0, s1) and y == s1 and dir.isUp():
        print('2 - top edge')
        return s2 - 1 - x, 0, Direction.Down
    # 2 - bottom edge
    elif x in range(s0, s1) and y == s2 - 1 and dir.isDown():
        print('2 - bottom edge')
        return s3 - 1 - x, s3 - 1, Direction.Up
    # 3 - top edge
    elif x in range(s1, s2) and y == s1 and dir.isUp():
        print('3 - top edge')
        return s2, x % size, Direction.Right
    # 3 - bottom edge
    elif x in range(s1, s2) and y == s2 - 1 and dir.isDown():
        print('3 - bottom edge')
        return s2, s2 + (x % size), Direction.Right
    # 4 - right edge
    elif x == s3 - 1 and y in range(s1, s2) and dir.isRight():
        print('4 - right edge')
        return s4 - 1 - (y % 4), s2, Direction.Down
    # 5 - left edge
    elif x == s2 and y in range(s2, s3) and dir.isLeft():
        print('5 - left edge')
        return s2 - 1 - (y % size), s2 - 1, Direction.Up
    # 5 - bottom edge
    elif x in range(s2, s3) and y == s3 - 1 and dir.isDown():
        print('5 - bottom edge')
        return s1 - 1 - (x % size), s2 - 1, Direction.Up
    # 6 - top edge
    elif x in range(s3, s4) and y == s2 and dir.isUp():
        print('6 - top edge')
        return s3 - 1, s2 - 1 - (x % size), Direction.Left
    # 6 - right edge
    elif x == s4 - 1 and y in range(s2, s3) and dir.isRight():
        print('6 - right edge')
        return s3 - 1, s1 - 1 - (y % size), Direction.Left
    # 6 - bottom edge
    elif x in range(s3, s4) and y == s3 - 1 and dir.isDown():
        print('6 - bottom edge')
        return 0, s2 - 1 - (x % size), Direction.Right

    return x if dir not in [Direction.Left, Direction.Right] else x + dir.step_amount(), \
            y if dir not in [Direction.Up, Direction.Down] else y + dir.step_amount(), \
            dir

def next_step_real():
    pass

def task_2():
    x, y = h_edges[0][0], 0
    dir = Direction.Right

    debug_map = [list(x) for x in map]
    debug_dir = ['>', 'v', '<', '^']

    print(x, y, dir)
    for ins in commands:
        print('ins:', ins)
        if isinstance(ins, int):
            for _ in range(ins):
                debug_map[y][x] = debug_dir[dir.value]
                next_x, next_y, next_dir = next_step_sample(x, y, dir) if use_sample else next_step_real(x, y, dir)
                if map[next_y][next_x] == '#':
                    break
                x, y, dir = next_x, next_y, next_dir
                print(x, y, dir)
        else:
            dir = dir.turn(dir_change[ins])
            print('turn:', dir)

    print(''.join([''.join(x) + '\n' for x in debug_map]))
    print('task 2:', 1000 * (y + 1) + 4 * (x + 1) + dir)

# task_1()
task_2()