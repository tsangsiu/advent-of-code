def merge_ranges(ranges):
    if not ranges:
        return []

    sorted_ranges = sorted(ranges)
    merged_ranges = [sorted_ranges[0]]

    for r in sorted_ranges[1:]:
        if r[0] <= merged_ranges[-1][1] or r[0] == merged_ranges[-1][1] + 1:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], r[1])
        else:
            merged_ranges.append(r)

    return merged_ranges

with open("./input.txt") as input:
    input = input.read().strip()
    ranges, ids = input.split("\n\n")

ranges = ranges.split("\n")
ranges = [list(map(int, r.split("-"))) for r in ranges]

count = 0
merged_ranges = merge_ranges(ranges)
for r in merged_ranges:
    count += r[1] - r[0] + 1

print(count)