from collections import defaultdict

grid = open("inputs/day07.txt").read().split("\n")
beams = {grid[0].index("S"): 1}
splits = 0
for y, row in enumerate(grid):
    new_beams = defaultdict(int)
    for beam, count in beams.items():
        if row[beam] == "^":
            splits += 1
            new_beams[beam-1] += count
            new_beams[beam+1] += count
        else:
            new_beams[beam] += count
    beams = new_beams
print(f"a = {splits}")
print(f"b = {sum(beams.values())}")
