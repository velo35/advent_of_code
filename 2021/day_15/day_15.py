import heapq

input_file = 1 and 'real.txt' or 'sample.txt'

with open('2021/day_15/input/' + input_file) as f:
    input = f.read()

grid = [[int(x) for x in line]for line in input.splitlines()]

def shortest_path(grid, start, end):
    visited = set()
    to_visit = [(0, start)]

    while to_visit:
        cost, node = heapq.heappop(to_visit)

        if node == end:
            return cost

        if node not in visited:
            visited.add(node)
            i, j = node

            if i > 0:
                heapq.heappush(to_visit, (cost + grid[i - 1][j], (i - 1, j)))
            if i < len(grid) - 1:
                heapq.heappush(to_visit, (cost + grid[i + 1][j], (i + 1, j)))
            if j > 0:
                heapq.heappush(to_visit, (cost + grid[i][j - 1], (i, j - 1)))
            if j < len(grid[0]) - 1:
                heapq.heappush(to_visit, (cost + grid[i][j + 1], (i, j + 1)))

    return -1

def task_1():
    print("task 1:", shortest_path(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1)))

def task_2():
    new_grid = [[0] * (5 * len(grid[0])) for _ in range(5 * len(grid))]
    for i in range(len(grid)):
        new_grid[i][:len(grid[i])] = grid[i]

    for i, j in [(i, j) for i in range(5) for j in range(5) if i != 0 or j != 0]:
        for v in range(len(grid)):
            for h in range(len(grid[v])):
                val = new_grid[v][h] + i + j
                while val > 9: val -= 9
                new_grid[i * len(grid) + v][j * len(grid[v]) + h] = val
                    
    print("task 2:", shortest_path(new_grid, (0, 0), (len(new_grid) - 1, len(new_grid[0]) - 1)))

task_1()
task_2()