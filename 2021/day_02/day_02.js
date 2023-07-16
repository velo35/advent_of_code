const host = "http://127.0.0.1:8080/2021/day_2/input"
const input_file = 1 ? "real.txt" : "sample.txt"

function task_1(commands)
{
    const h = commands.filter(x => x[0] === 'forward').reduce((a, b) => a + b[1], 0)
    const v = commands.filter(x => x[0] !== 'forward').reduce((a, b) => a + (b[0] === 'up' ? -b[1] : b[1]), 0)

    return h * v
}

function task_2(commands)
{
    let h = 0, depth = 0, aim = 0
    commands.forEach(command => {
        const delta = command[1]
        switch (command[0]) {
            case 'forward':
                h += delta
                depth += aim * delta
                break
            default:
                aim += (command[0] === 'down' ? delta : -delta)
        }
    });
    return h * depth
}

(async function() {
    const response = await fetch(host + "/" + input_file)
    const input = await response.text()

    const commands = input.split('\n').map(x => {const y = x.split(' '); return [y[0], Number.parseInt(y[1], 10) ]})
    // console.log(task_1(commands))
    console.log(task_2(commands))
})()