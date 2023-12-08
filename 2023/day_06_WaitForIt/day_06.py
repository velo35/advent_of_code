import os, math

def task_1(races):
    wins = []
    for time, dist in races:
        discr = (time**2 - 4*dist) ** 0.5
        t1 = (time - discr) / 2
        t2 = (time + discr) / 2
        wins.append(1 + math.ceil(t2 - 1) - math.floor(t1 + 1))

    result, *rest = wins
    for v in rest:
        result *= v
    return result
        

if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), input_filename)) as f:
        input = f.read()

    times, distances = [[int(y) for y in x.split(':')[1].split()] for x in input.splitlines()]
    races = [(times[i], distances[i]) for i in range(len(times))]

    print('task 1:', task_1(races))
    print('task 2:', task_1([(int(''.join([str(t) for t in times])), int(''.join([str(d) for d in distances])))]))