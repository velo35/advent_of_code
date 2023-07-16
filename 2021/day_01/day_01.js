const host = "http://127.0.0.1:8080"
const input_file = 1 ? "real.txt" : "sample.txt"

function task_1(depths)
{
    return depths.map((depth, ndx) => ndx > 0 && depth > depths[ndx-1] ? 1 : 0).reduce((a, b) => a + b, 0)
}

function task_2(depths)
{
    return depths.map((depth, ndx) => ndx >= 3 && depth > depths[ndx-3] ? 1 : 0).reduce((a, b) => a + b, 0)
}

(async function() {
    const response = await fetch(host + "/" + input_file)
    const input = await response.text()

    const depths = input.split('\n').map(x => Number.parseInt(x, 10))
    console.log(task_1(depths))
    console.log(task_2(depths))
})()