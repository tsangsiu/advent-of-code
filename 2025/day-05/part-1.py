with open("./input.txt") as input:
    input = input.read().strip()
    ranges, ids = input.split("\n\n")

ranges = ranges.split("\n")
ranges = [list(map(int, r.split("-"))) for r in ranges]
ranges = [range(lower, upper + 1) for lower, upper in ranges]

ids = ids.split("\n")
ids = [int(id) for id in ids]

count = 0
for id in ids:
    for r in ranges:
        if id in r:
            count += 1
            break

print(count)