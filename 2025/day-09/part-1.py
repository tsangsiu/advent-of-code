def area(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

with open("./input.txt") as input:
    input = input.read().strip()

coords = input.split("\n")
coords = [tuple([int(coord) for coord in _coords.split(",")]) for _coords in coords]

area_to_pair = {}
for idx1, _coords1 in enumerate(coords[:-1]):
    for _coords2 in coords[idx1 + 1:]:
        area_to_pair[area(_coords1, _coords2)] = (_coords1, _coords2)

print(max(area_to_pair))