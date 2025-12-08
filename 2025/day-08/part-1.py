import math

def dist(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

with open("./input.txt") as input:
    input = input.read().strip()

coords_str = input.split("\n")
coords = [tuple([int(coord_str) for coord_str in coord_str.split(",")]) for coord_str in coords_str]

dist_to_coord = {}
for idx1, coord1 in enumerate(coords[:-1]):
    for coord2 in coords[idx1 + 1:]:
        dist_to_coord[dist(coord1, coord2)] = [coord1, coord2]

coord_to_circuit = {}
for coord in coords:
    coord_to_circuit[coord] = None

n = 0
for idx, dist in enumerate(sorted(dist_to_coord)):
    if idx >= 1000:
        break

    coords = dist_to_coord[dist]

    circuits = [coord_to_circuit[coord] for coord in coords if coord_to_circuit[coord]]
    if len(circuits) == 1:
        for coord in coords:
            coord_to_circuit[coord] = circuits[0]
    elif len(circuits) > 1:
        n += 1
        for coord, circuit in coord_to_circuit.items():
            if coord in coords or circuit in circuits:
                coord_to_circuit[coord] = n
    else:
        n += 1
        for coord in coords:
            coord_to_circuit[coord] = n

counts = {circuit: list(coord_to_circuit.values()).count(circuit)
            for circuit in set(list(coord_to_circuit.values()))}
del counts[None]
counts = list(sorted(counts.values(), reverse=True))
print(counts[0] * counts[1] * counts[2])