import itertools

grid = open("inputs/day04.txt").read().split("\n")

def movable(y, x):
    count = 0
    for dy, dx in itertools.product([-1, 0, 1], [-1, 0, 1]):
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == "@":
            count += 1
    return count < 5

res_a = 0
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "@":
            res_a += int(movable(y, x))

print(res_a)