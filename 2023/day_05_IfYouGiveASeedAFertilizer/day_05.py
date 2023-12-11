import os, bisect

def task_1(seeds, mappings):
    locations = []
    for seed in seeds:
        current = seed
        for m in mappings:
            for d, s, i in m:
                if current in range(s, s + i):
                    current = d + current - s
                    break
        locations.append(current)
    return min(locations)

def task_2(seeds, mappings):
    input_intervals = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

    for m in mappings:
        sorted_mappings = sorted([(s, s + i, d) for d, s, i, in m])
        source_intervals = list(sum([(f, l) for f, l, _ in sorted_mappings], ()))
        destinations = [d for _, _, d in sorted_mappings]
        output_intervals = []
        for a, b in input_intervals:
            a_i = bisect.bisect_right(source_intervals, a)
            b_i = bisect.bisect_left(source_intervals, b)
            prev_a = a

            if a_i < len(source_intervals):
                s, d = source_intervals[a_i] if a_i % 2 == 0 else source_intervals[a_i - 1], destinations[int(a_i / 2)]
                while a_i < b_i:
                    if a_i % 2 == 0:
                        output_intervals.append((prev_a, s))
                        prev_a = s
                    else:
                        output_intervals.append((d + prev_a - s, d + source_intervals[a_i] - s))
                        prev_a = source_intervals[a_i]
                    a_i += 1
                    if a_i < len(source_intervals):
                        s, d = source_intervals[a_i] if a_i % 2 == 0 else source_intervals[a_i - 1], destinations[int(a_i / 2)]

            if a_i % 2 == 0:
                output_intervals.append((prev_a, b))
            else:
                output_intervals.append((d + prev_a - s, d + b - s))
        input_intervals = [(a, b) for a, b in output_intervals if a != b]

    return min([x for x, _ in input_intervals])
                
if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), input_filename)) as f:
        input = f.read()

    sections = input.split('\n\n')
    seeds = [int(x) for x in sections[0].split(':')[1].split()]
    mappings = [[[int(x) for x in line.split()] for line in lines.splitlines()[1:]] for lines in sections[1:]]
    
    print('task 1:', task_1(seeds, mappings))
    print('task 2:', task_2(seeds, mappings))
