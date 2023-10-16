import re, itertools

def snailfish(s):
    return [int(x) if x.isnumeric() else x for x in re.split("(\[|\d+|,|\])", s) if x]

def explode(sfn): #sfn - snailfish number
    depth = 0
    prevIntNdx = None
    for i in range(len(sfn)):
        if isinstance(sfn[i], int):
            prevIntNdx = i
        elif sfn[i] == '[':
            depth += 1
        elif sfn[i] == ']':
            depth -= 1
        if depth > 4:
            v1, v2 = sfn[i + 1], sfn[i + 3]
            if prevIntNdx:
                sfn[prevIntNdx] += v1
            nextIntNdx = i + 4
            while nextIntNdx < len(sfn) and not isinstance(sfn[nextIntNdx], int):
                nextIntNdx += 1
            if nextIntNdx < len(sfn):
                sfn[nextIntNdx] += v2
            sfn[i:i+5] = [0]
            return True
    return False

def split(sfn):
    for i in range(len(sfn)):
        if isinstance(sfn[i], int) and sfn[i] >= 10:
            v1, v2 = sfn[i] // 2, sfn[i] // 2
            if sfn[i] % 2 == 1:
                v2 += 1
            sfn[i] = ']'
            for x in [v2, ',', v1, '[']:
                sfn.insert(i, x)
            return True
    return False

def reduce(snailfish_number):
    while True:
        if not explode(snailfish_number):
            if not split(snailfish_number):
                return snailfish_number
            
def add(sfn1, sfn2):
    return reduce(['['] + sfn1 + [','] + sfn2 + [']'])
            
def magnitude(sfn):
    return eval(''.join([str(x) for x in sfn]).replace('[', '(3*').replace(',', '+2*').replace(']', ')'))

def task_1(snailfish_numbers):
    current, *rest = snailfish_numbers
    for x in rest:
        current = add(current, x)
    return magnitude(current)

def task_2(sfns):
    return max([magnitude(add(sfns[x], sfns[y])) for x, y in itertools.product(range(len(sfns)), repeat=2) if x != y])

if __name__ == "__main__":
    use_sample = False
    input_file = use_sample and 'sample.txt' or 'real.txt'
    with open('2021/day_18_Snailfish/input/' + input_file) as f:
        input = f.read()

    snailfish_numbers = [snailfish(s) for s in input.splitlines()]

    print("task_1: ", task_1(snailfish_numbers))
    print("task_2: ", task_2(snailfish_numbers))
