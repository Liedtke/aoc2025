current, count_a, count_b = 50, 0, 0
for line in open("inputs/day01.txt").read().split("\n"):
    factor = 1 if line[0] == "R" else -1
    by = int(line[1:])
    previous = current
    current += factor * (by % 100)
    if current <= 0 or current >= 100:
        count_b += (previous != 0)
    count_b += by // 100
    current %= 100
    if current == 0:
        count_a += 1

print(f"a = {count_a}\nb = {count_b}")
