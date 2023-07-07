input_file = 1 and "real.txt" or "sample.txt"

with open("2021/day_7/input/" + input_file) as f:
    input = f.read()

distances = [int(x) for x in input.split(',')]
median = sorted(distances)[len(distances) // 2]
totalFuel = sum([abs(x - median) for x in distances])

print("task 1:", totalFuel)

mean = sum(distances) / len(distances)
k = round(mean) - 1
totalFuel = sum([sum(list(range(abs(k - x) + 1))) for x in distances])
print("task 2:", totalFuel)


