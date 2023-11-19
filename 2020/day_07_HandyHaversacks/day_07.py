import os, regex

def rec(bag_color, bags):
    count = 0

    # print('rec', bag_color)
    for k, v in bags[bag_color].items():
        # print(k, v)
        count += v + v * rec(k, bags)

    return count

def task_2(bags):
    return rec('shiny gold', bags)

def task_1(bags):
    bag_colors = ['shiny gold']

    i = 0
    while i < len(bag_colors):
        bag_color = bag_colors[i]
        for k, v in bags.items():
            # FIXME: this adds the same parent multiple times to the search list
            if bag_color in v.keys():
                bag_colors.append(k)
        i += 1
    return len(set(bag_colors)) - 1

if __name__ == "__main__":
    use_sample = False
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), 'input', input_filename)) as f:
        input = f.read()

    bags = dict()
    for line in input.splitlines():
        match = regex.match(r"(\w+ \w+) bags contain(( (\d+ \w+ \w+) bags?[,.])| no other bags.)+", line)
        bags[match.group(1)] = {a: int(b) for a, b in [regex.match(r"(\d+) (\w+ \w+)", x).group(2, 1) for x in match.captures(4)]}
    
    # print(bags)
    print('task 1: ', task_1(bags))
    print('task 2: ', task_2(bags))