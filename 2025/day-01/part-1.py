file_path = 'input.txt'

curr_num = 50
zero_count = 0

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        direction = line[0]
        distance = int(line.strip()[1:])

        if direction == 'L':
            curr_num -= distance
            curr_num %= 100
        elif direction == 'R':
            curr_num += distance
            curr_num %= 100

        if curr_num == 0:
            zero_count += 1

print(zero_count)