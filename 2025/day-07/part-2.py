with open("./input.txt") as input:
    input = input.read().strip()

rows = input.split("\n")

counts = [0] * len(rows[0])
counts[rows[0].index("S")] = 1

for row in rows[1:]:
    if row.find('^') < 0:
        continue

    for idx_col, col in enumerate(row):
        if col == "^":
            counts[idx_col - 1] += counts[idx_col]
            counts[idx_col + 1] += counts[idx_col]
            counts[idx_col] = 0


print(sum(counts))