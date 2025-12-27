grid = open("inputs/day07.txt").read().split("\n")
beams = set([grid[0].index("S")])
splits = 0
for y, row in enumerate(grid):
    new_beams = set()
    for beam in beams:
        if row[beam] == "^":
            splits += 1
            new_beams.add(beam-1)
            new_beams.add(beam+1)
        else:
            new_beams.add(beam)
    beams = new_beams
print(f"a = {splits}")
