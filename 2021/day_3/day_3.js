const file_source = "http://127.0.0.1:8080/2021/day_3/input"
const file_name = 1 ? "real.txt" : "sample.txt"

function frequencies(binary_numbers)
{
    const result = {}
    const binary_len = binary_numbers[0].length
    result.ones = new Array(binary_len).fill(0)
    result.zeros = new Array(binary_len).fill(0)
    for (const binary_num of binary_numbers) {
        for (let i = 0; i < binary_len; i++) {
            if (binary_num[i] === '0') {
                result.zeros[i]++
            }
            else {
                result.ones[i]++
            }
        }
    }

    return result
}

function task_1(binary_numbers)
{
    const frequenies = frequencies(binary_numbers)
    const binary_len = binary_numbers[0].length

    const gamma_binary = []
    const epsilon_binary = []
    for (let i = 0; i < binary_len; i++) {
        if (frequenies.ones[i] > frequenies.zeros[i]) {
            gamma_binary.push('1')
            epsilon_binary.push('0')
        }
        else {
            gamma_binary.push('0')
            epsilon_binary.push('1')
        }
    }

    const gamma = Number.parseInt(gamma_binary.join(''), 2)
    const epsilon = Number.parseInt(epsilon_binary.join(''), 2)

    return gamma * epsilon
}

function task_2(binary_numbers)
{
    const binary_len = binary_numbers[0].length

    let oxygens = [...binary_numbers]
    let co2s = [...binary_numbers]

    for (let i = 0; i < binary_len; i++) {
        if (oxygens.length > 1) {
            const of = frequencies(oxygens)
            if (of.ones[i] === of.zeros[i]) {
                oxygens = oxygens.filter(x => x[i] == '1')
                
            }
            else if (of.ones[i] > of.zeros[i]) {
                oxygens = oxygens.filter(x => x[i] == '1')
            }
            else {
                oxygens = oxygens.filter(x => x[i] == '0')
            }
        }
        if (co2s.length > 1) {
            const cf = frequencies(co2s)
            if (cf.ones[i] === cf.zeros[i]) {
                co2s = co2s.filter(x => x[i] == '0')
                
            }
            else if (cf.ones[i] < cf.zeros[i]) {
                co2s = co2s.filter(x => x[i] == '1')
            }
            else {
                co2s = co2s.filter(x => x[i] == '0')
            }
        }
    }

    const oxygen = Number.parseInt(oxygens[0], 2)
    const co2 = Number.parseInt(co2s[0], 2)

    return oxygen * co2
}


(async function() 
{
    const response = await fetch(file_source + "/" + file_name)
    const input = await response.text()

    const binary_numbers = input.split('\n')
    console.log(task_1(binary_numbers))
    console.log(task_2(binary_numbers))
})()