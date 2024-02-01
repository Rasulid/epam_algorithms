def bitmask(args: list):
    n = len(args)
    combinations = []
    count = 0
    for mask in range(1 << n):
        current_combination = []
        for i in range(n):
            if mask & (1 << i):
                current_combination.append(args[i])
        combinations.append(current_combination)
        count += 1
    print(count)
    return combinations


l = [1, 2, 3, 4]
result = bitmask(l)
for combo in result:
    print(combo)
