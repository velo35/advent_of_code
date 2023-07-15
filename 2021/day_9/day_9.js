const source = "http://127.0.0.1:8080/input/"
const input_file = 1 ? "real.txt" : "sample.txt"

function find_low_points(grid)
{
    const low_points = []

    for (i = 0; i < grid.length; i++) {
        for (j = 0; j < grid[0].length; j++) {
            let is_low = true
            if (i > 0) {
                is_low &= grid[i - 1][j] > grid[i][j]
            }
            if (i < grid.length - 1) {
                is_low &= grid[i + 1][j] > grid[i][j]
            }
            if (j > 0) {
                is_low &= grid[i][j - 1] > grid[i][j]
            }
            if (j < grid[0].length - 1) {
                is_low &= grid[i][j + 1] > grid[i][j]
            }

            if (is_low) {
                low_points.push([i, j])
            }
        }
    }

    return low_points
}

function task_1(grid)
{
    const low_points = find_low_points(grid)
    let total_risk = 0

    for (let [i, j] of low_points) {
        total_risk += grid[i][j] + 1
    }

    return total_risk
}

function find_basin_size(i, j, grid)
{
    const visited = new Set()
    const to_visit = [[i, j]]
    let basin_size = 0

    while (to_visit.length > 0) {
        let [v, h] = to_visit.shift()
        const current = JSON.stringify([v, h])
        if (!visited.has(current)) {
            visited.add(current)
            basin_size++;

            if (v > 0 && grid[v - 1][h] !== 9) {
                to_visit.push([v - 1, h])
            }
            if (v < grid.length - 1 && grid[v + 1][h] !== 9) {
                to_visit.push([v + 1, h])
            }
            if (h > 0 && grid[v][h - 1] !== 9) {
                to_visit.push([v, h - 1])
            }
            if (h < grid[0].length - 1 && grid[v][h + 1] !== 9) {
                to_visit.push([v, h + 1])
            }
        }
    }

    return basin_size
}

function task_2(grid)
{
    const low_points = find_low_points(grid)
    const basin_sizes = []

    for (let [i, j] of low_points) {
        basin_sizes.push(find_basin_size(i, j, grid))
    }

    basin_sizes.sort((a, b) => b - a)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
}

function solve(input)
{
    const lines = input.split('\n')
    const grid = []

    for (let line of lines) {
        grid.push(line.match(/\d/g).map(x => Number.parseInt(x, 10)))
    }
    
    console.log("task 1:", task_1(grid))
    console.log("task 2:", task_2(grid))
}

fetch(source + input_file)
    .then(response => response.text())
    .then(input => solve(input))