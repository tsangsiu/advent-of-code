from itertools import chain, combinations

def power_set(lst: list) -> list:
    return list(chain.from_iterable(combinations(lst, l) for l in range(1, len(lst) + 1)))

def combo_to_light_status(combo: list) -> list:
    combo = [light for schema in combo for light in schema]
    combo = {light: combo.count(light) for light in set(combo)}
    return sorted([light for light, count in combo.items() if count % 2 == 1])

def diagram_to_light_status(diagram: str) -> list:
    return sorted([idx for idx, light in enumerate(diagram) if light == "#"])

#####

with open("./input.txt") as input:
    input = input.read().strip()

machines = input.split("\n")
n_machines = len(machines)

diagrams = []; schemas = []; joltages = []
for machine in machines:
    machine = machine.split(" ")

    diagrams.append(machine[0][1:-1])

    schemas.append([])
    for schema in machine[1:-1]:
        schemas[-1].append([])
        for light in schema[1:-1].split(","):
            schemas[-1][-1].append(int(light))
        schemas[-1][-1] = tuple(schemas[-1][-1])

    joltages.append([])
    for joltage in machine[-1][1:-1].split(","):
        joltages[-1].append(int(joltage))

#####

fewest_button_presses_required = 0
for idx_machine in range(n_machines):
    diagram = diagrams[idx_machine]
    light_status = diagram_to_light_status(diagram)
    schema = schemas[idx_machine]
    schema_combos = sorted(power_set(schema), key=len)

    for schema_combo in schema_combos:
        if combo_to_light_status(schema_combo) == light_status:
            fewest_button_presses_required += len(schema_combo)
            break
        
print(fewest_button_presses_required)