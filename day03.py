sum_a = 0
for bank in open("inputs/day03.txt").read().split("\n"):
    first = max(bank[:-1])
    index = bank.index(first)
    second = max(bank[index+1:])
    sum_a += int(first + second)
print(f"a = {sum_a}")
