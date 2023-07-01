const source = "http://127.0.0.1:8080/2021/day_4/input"
const input_file = 1 ? "real.txt" : "sample.txt"

function task(calls, boards, task)
{
    const boards_info = []

    for (let i = 0; i < boards.length; i++) {
        boards_info.push({
            remaining: [...boards[i]],
            rows: Array(5).fill(0),
            cols: Array(5).fill(0)
        })
    }

    let win_count = 0
    let boards_without_wins = Array(boards.length).fill(true)

    for (const call of calls) {
        for (let i = 0; i < boards.length; i++) {
            const index = boards[i].indexOf(call)
            if (index !== undefined && boards_without_wins[i]) {
                const board_info = boards_info[i]
                const row = Math.floor(index / 5)
                const col = index % 5
                board_info.remaining = board_info.remaining.filter(x => x != call)
                board_info.rows[row]++
                board_info.cols[col]++
                if (board_info.rows[row] == 5 || board_info.cols[col] == 5) {
                    if (task == 1 || win_count == boards.length - 1) {
                        return call * board_info.remaining.reduce((a, b) => a + b, 0)
                    }
                    win_count++
                    boards_without_wins[i] = false
                }
            }
        }
    }
}

function solve(input)
{
    const lines = input.split('\n')

    const calls = lines[0].match(/\d+/g).map(x => Number.parseInt(x, 10))
    const boards = []

    for (let i = 2; i < lines.length; i += 6) {
        boards.push(lines.slice(i, i + 5).join().match(/\d+/g).map(x => Number.parseInt(x, 10)))
    }

    console.log("task1:", task(calls, boards, 1))
    console.log("task2:", task(calls, boards, 2))
}

fetch(source + "/" + input_file)
    .then(response => response.text())
    .then(input => solve(input))

