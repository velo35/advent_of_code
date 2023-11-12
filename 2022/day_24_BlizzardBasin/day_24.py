import math
from itertools import product

def all_blizzard_positions(map):
    w, h = len(map[0]), len(map)
    cycle_len = math.lcm(w, h)

    d_s = {'<': (-1, 0), '^': (0, -1), '>': (1, 0), 'v': (0, 1)}
    blizzards = [(j, i, d_s[map[i][j]]) for i, j in product(range(h), range(w)) if map[i][j] in d_s]
    
    return [{((x + dx*t) % w, (y + dy*t) % h) for x, y, (dx, dy) in blizzards} for t in range(cycle_len)]

def possible_positions(map):
    w, h = len(map[0]), len(map)
    return {pos for pos in product(range(w), range(h))} | {(0, -1), (w - 1, h)}

def all_possible_positions(map):
    pp = possible_positions(map)
    abp = all_blizzard_positions(map)

    return [pp - bp for bp in abp]

def search_bfs(all_positions, start, finish, t0 = 0):
    cycle_len = len(all_positions)
    visited = [set() for t in range(cycle_len)]
    to_visit = [(start, t0)]

    while to_visit:
        pos, t = to_visit.pop(0)
        if pos not in visited[t % cycle_len]:
            visited[t % cycle_len].add(pos)

            for next in [(pos[0] + dx, pos[1] + dy) for dx, dy in [(1, 0), (0, 1), (0, 0), (-1, 0), (0, -1)]]:
                if next == finish:
                    return t + 1
                elif next in all_positions[(t + 1) % cycle_len]:
                    to_visit.append((next, t + 1))
    return math.inf

def task_1(map):
    w, h = len(map[0]), len(map)
    return search_bfs(all_possible_positions(map), (0, -1), (w - 1, h))

def task_2(map):
    pp = all_possible_positions(map)
    w, h = len(map[0]), len(map)
    begin = (0, -1)
    end = (w - 1, h)

    t1 = search_bfs(pp, begin, end)
    t2 = search_bfs(pp, end, begin, t1)
    return search_bfs(pp, begin, end, t2)


if __name__ == "__main__":
    use_sample = False
    input_file = use_sample and 'sample.txt' or 'real.txt'
    with open('2022/day_24_BlizzardBasin/input/' + input_file) as f:
        input = f.read()

    map = [line[1:-1] for line in input.splitlines()[1:-1]]

    print('task 1: ', task_1(map))
    print('task 2: ', task_2(map))

    