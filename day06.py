from functools import reduce
import operator
filename = "inputs/day06.txt"
lines = [l.split(" ") for l in open(filename).read().split("\n")]
lines = [[e for e in line if e != ""] for line in lines]
ops = lines[-1]
nums = [[int(e) for e in line] for line in lines[:-1]]
print(f"a = {sum(reduce(operator.mul if op == "*" else operator.add, operands) for operands, op in zip(zip(*nums), ops))}")

lines = open(filename).read().split("\n")[:-1]
nums = ["".join(col).strip() for col  in zip(*lines)]
parsed_nums, curr = [], []
for num in nums:
    if num == "":
        parsed_nums.append(curr)
        curr = []
    else:
        curr.append(int(num))
parsed_nums.append(curr)
print(f"b = {sum(reduce(operator.mul if op == "*" else operator.add, operands) for operands, op in zip(parsed_nums, ops))}")
