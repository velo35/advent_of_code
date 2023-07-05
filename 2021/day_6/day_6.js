const source = "http://127.0.0.1:8080/2021/day_6/input"
const input_file = 1 ? "real.txt" : "sample.txt"

function task_1(ages, days)
{
    for (let i = days; i > 0; i--) {
        const new_fish = []
        for (let j = 0; j < ages.length; j++) {
            ages[j]--;
            if (ages[j] < 0) {
                ages[j] = 6
                new_fish.push(8)
            }
        }
        ages = ages.concat(new_fish)
    }

    return ages.length
}

function task_2(ages, days)
{
    function count_fish(days_left, lookup)
    {
        let count = 0

        if (lookup[days_left] !== undefined) {
            count = lookup[days_left]
        }
        else {
            for (let i = 0; i < days_left; i += 7) {
                count += count_fish(days_left - i - 9, lookup) + 1
            }

            lookup[days_left] = count
        }

        return count
    }

    let count = ages.length
    const lookup = {}

    for (const age of ages) {
        count += count_fish(days - age, lookup)
    }

    return count
}

function solve(input)
{
    const ages = input.match(/\d+/g).map(x => Number.parseInt(x, 10))
    
    console.log("task 1:", task_1([...ages], 80))
    console.log("task 2:", task_2(ages, 256))
}

fetch(source + "/" + input_file)
    .then(response => response.text())
    .then(input => solve(input))