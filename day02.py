invalid_ids = []
for range in (r.split("-") for r in open("inputs/day02.txt").read().split(",")):
    print(range)
    lower_i, upper_i = (int(i) for i in range)
    digits = len(range[0]) // 2 + (len(range[0]) % 2)
    max_digits = len(range[1]) // 2
    n = lower_i // (10 ** digits)

    while digits <= max_digits:
        num = n * (10 ** digits) + n
        if lower_i <= num <= upper_i:
            invalid_ids.append(num)
        if num > upper_i:
            break
        n += 1
        if n >= 10 ** digits:
            digits += 1

    print(invalid_ids)
    print(sum(invalid_ids))
print(f"a = {sum(set(invalid_ids))}")
