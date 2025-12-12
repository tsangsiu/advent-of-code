from functools import cache

with open("./input.txt") as input:
    input = input.read().strip()

lines = input.split("\n")

map = {}
for line in lines:
    line = line.split(": ")
    map[line[0]] = line[1].split(" ")

@cache
def dfs(st, dest):
    if st == dest:
        return 1
    else:
        return sum(dfs(node, dest) for node in map.get(st, []))

print(dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out") + \
      dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out"))