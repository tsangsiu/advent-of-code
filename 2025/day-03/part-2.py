with open("./input.txt") as input:
    input = input.read().strip()
    banks = input.split("\n")

n_batteries = 12

sum = 0
for bank in banks:
    max_joltage = ""

    for i in range(n_batteries):
        if len(bank) > n_batteries - i:
            max_digit = max(bank[:len(bank) - (n_batteries - i) + 1])
            max_digit_idx = bank[:len(bank) - (n_batteries - i) + 1].index(max_digit)
            bank = bank[max_digit_idx + 1:]
            max_joltage += max_digit
        else:
            max_joltage += bank
            break

    sum += int(max_joltage)

print(sum)