with open("./input.txt") as input:
    input = input.read().strip()
    ranges = input.split(",")

sum = 0

ranges = [[int(limit) for limit in range.split("-")] for range in ranges]
for r in ranges:
    lower, upper = r

    for id in range(lower, upper + 1):
        id_str = str(id)   
        id_len = len(id_str)

        for curr_len in range(1, id_len):
            if id_len % curr_len != 0:
                next

            _id_str = id_str
            while _id_str != "":
                if _id_str[:curr_len] == id_str[:curr_len]:
                    _id_str = _id_str[curr_len:]
                else:
                    break

                if _id_str == "":
                    sum += id

            if _id_str == "":
                break

print(sum)