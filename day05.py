from bisect import bisect_left

ranges, items = open("inputs/day05.txt").read().split("\n\n")
items = [int(item) for item in items.split("\n")]
ranges = [[int(n) for n in r.split("-")] for r in ranges.split("\n")]
ranges.sort()
# Merge all overlapping ranges.
merged_ranges = []
current = ranges[0]
for i, r in enumerate(ranges):
    if r[0] > current[1] + 1:
        merged_ranges.append(tuple(current))
        current = r
    else:
        current[1] = max(current[1], r[1])
merged_ranges.append(tuple(current))

def fresh(item):
    l, h = merged_ranges[max(bisect_left(merged_ranges, (item, item))-1, 0)]
    return l <= item <= h

print(f"a = {sum(1 if fresh(item) else 0 for item in items)}")
print(f"b = {sum(r[1] - r[0] + 1 for r in merged_ranges)}")
