const source = "http://127.0.0.1:8080/2021/day_5/input"
const input_file = 1 ? "real.txt" : "sample.txt"

function task(input, task_id)
{
    const grid = {}

    for (const line of input.split('\n')) {
        const [x0, y0, x1, y1] = line.match(/\d+/g).map(x => Number.parseInt(x, 10))
        
        if (x0 == x1) {
            const dy = y1 > y0 ? 1 : -1
            for (let i = y0; i != y1; i += dy) {
                const pos = `${x0},${i}`
                grid[pos] = grid[pos] ? grid[pos] + 1 : 1
            }
            const pos = `${x0},${y1}`
            grid[pos] = grid[pos] ? grid[pos] + 1 : 1
        }
        else if (y0 == y1) {
            const dx = x1 > x0 ? 1 : -1
            for (let i = x0; i != x1; i += dx) {
                const pos = `${i},${y0}`
                grid[pos] = grid[pos] ? grid[pos] + 1 : 1
            }
            const pos = `${x1},${y0}`
            grid[pos] = grid[pos] ? grid[pos] + 1 : 1
        }
        else if (task_id == 2) {
            const dx = x1 > x0 ? 1 : -1
            const dy = y1 > y0 ? 1 : -1

            let j = y0
            for (let i = x0; i != x1; i += dx, j += dy) {
                const pos = `${i},${j}`
                grid[pos] = grid[pos] ? grid[pos] + 1 : 1
            }
            const pos = `${x1},${y1}`
            grid[pos] = grid[pos] ? grid[pos] + 1 : 1
        }
    }

    return Object.entries(grid).filter(x => x[1] > 1).length
}

function solve(input)
{
    console.log("task1:", task(input, 1))
    console.log("task2:", task(input, 2))
}

fetch(source + "/" + input_file)
    .then(response => response.text())
    .then(input => solve(input))