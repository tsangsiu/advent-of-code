with open("./input.txt") as input:
    input = input.read().strip()
    banks = input.split("\n")

sum = 0
for bank in banks:
    max_joltage = max(bank[:len(bank) - 1])
    idx = bank.index(max_joltage)
    max_joltage += max(bank[idx + 1:])

    sum += int(max_joltage)

print(sum)