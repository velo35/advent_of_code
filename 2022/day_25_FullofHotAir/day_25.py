import os

decode = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2
}

def decoder(x):
    return decode[x]

encode = {v: k for k, v in decode.items()}

def encoder(x):
    return encode[x]

def snafu_add_d(*args):
    carry = 0
    v = sum(args)
    if v > 2:
        carry = 1
        v -= 5
    elif v < -2:
        carry = -1
        v += 5
    return v, carry

def snafu_add_r(a, b):
    carry = 0
    big, small = len(a) > len(b) and (a, b) or (b, a)

    for i in range(len(small)):
        big[i], carry = snafu_add_d(big[i], small[i], carry)

    if carry != 0:
        for i in range(len(small), len(big)):
            big[i], carry = snafu_add_d(big[i], carry)

        if carry != 0:
            big.append(carry)            

    return big

def task_1(snafu_nums):
    # Either add the numbers in snafu space or convert to decimal, add, and then convert back to snafu. I've opted for the former
    result, *rest = [list(map(decoder, reversed(v))) for v in snafu_nums]
    for i, num in enumerate(rest):
        result = snafu_add_r(result, num)

    return ''.join(map(encoder, reversed(result)))

if __name__ == "__main__":
    use_sample = False
    input_file = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), 'input', input_file)) as f:
        input = f.read()
    
    snafu_nums = input.splitlines()
    print("task_1: ", task_1(snafu_nums))