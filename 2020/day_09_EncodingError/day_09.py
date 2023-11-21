import os

def task_1(nums, pre):
    sums = [[nums[i] + nums[j] for j in range(i + 1, pre)] for i in range(pre - 1)]

    for i in range(pre, len(nums)):
        if all(nums[i] not in nsum for nsum in sums):
            return nums[i]
        sums = sums[1:] + [[]]
        for j, k in enumerate(nums[i - pre + 1: i]):
            sums[j].append(k + nums[i])
        
    return -1

def task_2(nums, target):
    i, j = 0, 0
    tsum = nums[0]

    while True:
        if tsum > target:
            tsum -= nums[i]
            i += 1
        elif tsum < target:
            j += 1
            tsum += nums[j]
        else:
            return min(nums[i:j+1]) + max(nums[i:j+1])

if __name__ == "__main__":
    use_sample = False
    pre = use_sample and 5 or 25
    input_filename = use_sample and 'sample.txt' or 'real.txt'
    with open(os.path.join(os.path.dirname(__file__), 'input', input_filename)) as f:
        input = f.read()

    nums = [int(x) for x in input.splitlines()]
    print("task 1:", task_1(nums, pre))
    print("task 1:", task_2(nums, task_1(nums, pre)))