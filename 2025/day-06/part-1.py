with open("./input.txt") as input:
    input = input.read().strip()

input = input.split("\n")
input = [row.split() for row in input]

nums = input[:-1]
nums = [[int(num) for num in row] for row in nums]

ops = input[-1]

total = 0
for idx in range(len(ops)):
    op = ops[idx]

    if op == "+":
        sum = 0
        for row in range(len(nums)):
            sum += nums[row][idx]
        total += sum

    elif op == "*":
        prod = 1
        for row in range(len(nums)):
            prod *= nums[row][idx]
        total += prod

print(total)