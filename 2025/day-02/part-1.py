with open("./input.txt") as input:
    input = input.read().strip()
    ranges = input.split(",")

sum = 0

ranges = [[int(limit) for limit in range.split("-")] for range in ranges]
for r in ranges:
    lower, upper = r

    for id in range(lower, upper + 1):
        id_str = str(id)

        if len(id_str) % 2 == 0:
            mid = len(id_str) // 2
            if id_str[:mid] == id_str[mid:]:
                sum += id

print(sum)