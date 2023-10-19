import re
from collections import namedtuple
from enum import IntEnum

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
        return self == Direction.Up
    
    def turn(self, ins):
        dir_change = {'L': -1, 'R': 1}
        amt = dir_change[ins]
        return [Direction.Right, Direction.Down, Direction.Left, Direction.Up][(self.value + amt) % 4]

    def step_amount(self):
        return 1 if self in [Direction.Right, Direction.Down] else -1

def init(use_sample):
    input_file = 'sample.txt' if use_sample else 'real.txt'
    with open('2022/day_22/input/' + input_file) as f:
        input = f.read().splitlines()
    map = input[:-2]
    commands = [int(x) if x not in 'LR' else x for x in re.findall('(\d+|L|R)', input[-1])]

    max_len = max([len(line) for line in map])
    map = [line + ' ' * (max_len - len(line)) for line in map] # need to do this for v_edges
    return map, commands

def task_1(map, commands):
    Boundary = namedtuple('Boundary', 'first last')
    h_edges = [Boundary(f, l - 1) for f, l in [re.search('\S+', line).span() for line in map]]
    v_edges = [Boundary(f, l - 1) for f, l in [re.search('\S+', line).span() for line in [''.join(x) for x in zip(*map)]]]
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
            dir = dir.turn(ins)

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
        return s1 + y, s1, Direction.Down
    # 1 - top edge
    elif x in range(s2, s3) and y == 0 and dir.isUp():
        return s1 - 1 - (x % size), s1, Direction.Down
    # 1 - right edge
    elif x == s3 - 1 and y in range(s0, s1) and dir.isRight():
        return s4 - 1, s3 - 1 - y, Direction.Left
    # 2 - left edge
    elif x == 0 and y in range(s1, s2) and dir.isLeft():
        return s4 - 1 - (y % size), s2 - 1, Direction.Up
    # 2 - top edge
    elif x in range(s0, s1) and y == s1 and dir.isUp():
        return s2 - 1 - x, 0, Direction.Down
    # 2 - bottom edge
    elif x in range(s0, s1) and y == s2 - 1 and dir.isDown():
        return s3 - 1 - x, s3 - 1, Direction.Up
    # 3 - top edge
    elif x in range(s1, s2) and y == s1 and dir.isUp():
        return s2, x % size, Direction.Right
    # 3 - bottom edge
    elif x in range(s1, s2) and y == s2 - 1 and dir.isDown():
        return s2, s2 + (x % size), Direction.Right
    # 4 - right edge
    elif x == s3 - 1 and y in range(s1, s2) and dir.isRight():
        return s4 - 1 - (y % 4), s2, Direction.Down
    # 5 - left edge
    elif x == s2 and y in range(s2, s3) and dir.isLeft():
        return s2 - 1 - (y % size), s2 - 1, Direction.Up
    # 5 - bottom edge
    elif x in range(s2, s3) and y == s3 - 1 and dir.isDown():
        return s1 - 1 - (x % size), s2 - 1, Direction.Up
    # 6 - top edge
    elif x in range(s3, s4) and y == s2 and dir.isUp():
        return s3 - 1, s2 - 1 - (x % size), Direction.Left
    # 6 - right edge
    elif x == s4 - 1 and y in range(s2, s3) and dir.isRight():
        return s3 - 1, s1 - 1 - (y % size), Direction.Left
    # 6 - bottom edge
    elif x in range(s3, s4) and y == s3 - 1 and dir.isDown():
        return 0, s2 - 1 - (x % size), Direction.Right

    return x if dir not in [Direction.Left, Direction.Right] else x + dir.step_amount(), \
            y if dir not in [Direction.Up, Direction.Down] else y + dir.step_amount(), \
            dir

def next_step_real(x, y, dir):
    size = 50
    s0 = 0 * size
    s1 = 1 * size
    s2 = 2 * size
    s3 = 3 * size
    s4 = 4 * size

    # 1 - top edge
    if x in range(s1, s2) and y == 0 and dir.isUp():
        return 0, s3 + x % size, Direction.Right
    # 1 - left edge
    elif x == s1 and y in range(s0, s1) and dir.isLeft():
        return 0, s3 - 1 - (y % size), Direction.Right
    # 2 - top edge
    elif x in range(s2, s3) and y == 0 and dir.isUp():
        return s0 + (x % size), s4 - 1, Direction.Up 
    # 2 - right edge
    elif x == s3 - 1 and y in range(s0, s1) and dir.isRight():
        return s2 - 1, s3 - 1 - (y % size), Direction.Left
    # 2 - bottom edge
    elif x in range(s2, s3) and y == s1 - 1 and dir.isDown():
        return s2 - 1, s1 + (x % size), Direction.Left
    # 3 - left edge
    elif x == s1 and y in range(s1, s2) and dir.isLeft():
        return s0 + (y % size), s2, Direction.Down
    # 3 - right edge
    elif x == s2 - 1 and y in range(s1, s2) and dir.isRight():
        return s2 + (y % size), s1 - 1, Direction.Up
    # 4 - left edge
    elif x == 0 and y in range(s2, s3) and dir.isLeft():
        return s1, s1 - 1 - (y % size), Direction.Right
    # 4 - top edge
    elif x in range(s0, s1) and y == s2 and dir.isUp():
        return s1, s1 + (x % size), Direction.Right
    # 5 - right edge
    elif x == s2 - 1 and y in range(s2, s3) and dir.isRight():
        return s3 - 1, s1 - 1 - (y % size), Direction.Left
    # 5 - bottom edge
    elif x in range(s1, s2) and y == s3 - 1 and dir.isDown():
        return s1 - 1, s3 + (x % size), Direction.Left
    # 6 - left edge
    elif x == 0 and y in range(s3, s4) and dir.isLeft():
        return s1 + (y % size), 0, Direction.Down
    # 6 - right edge
    elif x == s1 - 1 and y in range(s3, s4) and dir.isRight():
        return s1 + (y % size), s3 - 1, Direction.Up
    # 6 - bottom edge
    elif x in range(s0, s1) and y == s4 - 1 and dir.isDown():
        return s2 + (x % size), 0, Direction.Down

    return x if dir not in [Direction.Left, Direction.Right] else x + dir.step_amount(), \
            y if dir not in [Direction.Up, Direction.Down] else y + dir.step_amount(), \
            dir

def task_2(map, commands, use_sample):
    x, y = map[0].find('.'), 0
    dir = Direction.Right

    for ins in commands:
        if isinstance(ins, int):
            for _ in range(ins):
                next_x, next_y, next_dir = next_step_sample(x, y, dir) if use_sample else next_step_real(x, y, dir)
                if map[next_y][next_x] == '#':
                    break
                x, y, dir = next_x, next_y, next_dir
        else:
            dir = dir.turn(ins)

    print('task 2:', 1000 * (y + 1) + 4 * (x + 1) + dir)

if __name__ == "__main__":
    use_sample = False
    map, commands = init(use_sample)
    task_1(map, commands)
    task_2(map, commands, use_sample)