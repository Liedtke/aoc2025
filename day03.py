def solve(bank, digits):
    if digits == 1:
        return max(bank)
    first = max(bank[:-digits+1])
    index = bank.index(first)
    tail = solve(bank[index+1:], digits-1)
    return first + tail

banks = open("inputs/day03.txt").read().split("\n")
print(f"a = {sum(int(solve(bank, 2)) for bank in banks)}")
print(f"b = {sum(int(solve(bank, 12)) for bank in banks)}")
