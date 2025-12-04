def print_grid(grid):
    for row in grid:
        print(''.join(row))

with open("./input.txt") as input:
    input = input.read().strip()
    grid = input.split("\n")

n_row = len(grid)
n_col = len(grid[0])

grid = [list('.' + row + '.') for row in grid]
grid.insert(0, ['.'] * (n_col + 2))
grid.append(['.'] * (n_col + 2))

total = 0

while True:
    to_remove = []

    for row in range(1, n_row + 1):
        for col in range(1, n_col + 1):
            if grid[row][col] != '@':
                continue

            count = 0
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]:
                if grid[row + dr][col + dc] == '@':
                    count += 1

            if count < 4:
                total += 1
                to_remove.append((row, col))

    if to_remove == []:
        break

    for row, col in to_remove:
        grid[row][col] = '.'

print(total)