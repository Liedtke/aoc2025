import math
import heapq
import operator
from functools import reduce
boxes = [tuple(map(int, line.split(","))) for line in open("inputs/day08.txt").read().split("\n")]
distances = []
for i, a in enumerate(boxes):
    for b in boxes[i+1:]:
        dist = math.sqrt(sum((x[0] - x[1]) ** 2 for x in zip(a, b)))
        distances.append((dist, a, b))

heapq.heapify(distances)
grids = {box: set([box]) for box in boxes}
for i in range(1, 1_000_000):
    distance, a, b = heapq.heappop(distances)
    new_grid = grids[a].union(grids[b])
    for point in new_grid:
        grids[point] = new_grid
    if i == 1_000:
        unique_grids = set(map(tuple, grids.values()))
        sizes = list(reversed(sorted([len(grid) for grid in unique_grids])))
        print(f"a = {reduce(operator.mul, sizes[:3])}")
    if len(new_grid) == len(boxes):
        print(f"b = {a[0] * b[0]}")
        break
