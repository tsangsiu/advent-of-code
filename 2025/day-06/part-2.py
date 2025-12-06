def prod(nums):
    prod = 1

    for num in nums:
        prod *= num

    return prod

with open("./input.txt") as input:
    input = input.read().strip()

input = input.split("\n")

rows = input[:-1]
ops = input[-1].split()

total = 0
idx_ops = 0
nums = []
for idx_col in range(len(rows[0])):
    for idx_row, row in enumerate(rows):
        if idx_row == 0:
            nums.append(row[idx_col])
        else:
            nums[-1] += row[idx_col]

    if nums[-1].strip() == "":
        nums = [int(num) for num in nums[:-1]]

        if ops[idx_ops] == "+":
            total += sum(nums)
        elif ops[idx_ops] == "*":
            total += prod(nums)
        
        nums = []
        idx_ops += 1

nums = [int(num) for num in nums]
        
if ops[idx_ops] == "+":
    total += sum(nums)
elif ops[idx_ops] == "*":
    total += prod(nums)

print(total)