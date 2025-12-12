with open("./input.txt") as input:
    input = input.read().strip()

lines = input.split("\n")

map = {}
for line in lines:
    line = line.split(": ")
    map[line[0]] = line[1].split(" ")

count = 0
stack = ["fft"]
while stack != []:
    print(len(stack))
    node = stack.pop()
    for neighbor in map[node]:
        if neighbor == "out":
            count += 1
        else:
            stack.append(neighbor)

print(count)