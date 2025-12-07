with open("./input.txt") as input:
    input = input.read().strip()

rows = input.split("\n")

count_split = 0
idxs_beam = {rows[0].index("S")}

for row in rows[1:]: 
    if row.find('^') < 0:
        continue

    idxs_beam_next = set()
    for idx in idxs_beam:
        if row[idx] == '^':
            count_split += 1
            idxs_beam_next.add(idx - 1)
            idxs_beam_next.add(idx + 1)
        else:
            idxs_beam_next.add(idx)
    
    idxs_beam = idxs_beam_next

print(count_split)