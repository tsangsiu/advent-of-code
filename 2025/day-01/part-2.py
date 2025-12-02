file_path = 'input.txt'

curr_num = 50
zero_count = 0

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        direction = line[0]
        distance = int(line.strip()[1:])

        rotation_count, distance = divmod(distance, 100)
        zero_count += rotation_count

        if direction == 'L':
            next_num = curr_num - distance
        elif direction == 'R':
            next_num = curr_num + distance

        if curr_num * next_num < 0 or next_num > 100:   # the logic to check crossing 0
            zero_count += 1
        if next_num % 100 == 0:
            zero_count += 1
        
        curr_num = next_num % 100

print(zero_count)