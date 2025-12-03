with open("./input.txt") as input:
    input = input.read().strip()
    ranges = input.split(",")

ranges = [range.split("-") for range in ranges]
nums = [num for lower, upper in ranges for num in list(range(int(lower), int(upper) + 1))]

sum = 0
for num in nums:
    s = str(num)
    for curr_len in range(2, len(s) + 1):
        if len(s) % curr_len != 0:
            next

        if s[:len(s) // curr_len] * curr_len == s:
            sum += num
            break

print(sum)