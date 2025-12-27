from functools import reduce
import operator

lines = [l.split(" ") for l in open("inputs/day06.txt").read().split("\n")]
lines = [[e for e in line if e != ""] for line in lines]
ops = lines[-1]
nums = [[int(e) for e in line] for line in lines[:-1]]
print(f"a = {sum(reduce(operator.mul if op == "*" else operator.add, operands) for operands, op in zip(zip(*nums), ops))}")
