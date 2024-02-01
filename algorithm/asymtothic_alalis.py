def cycle_ij(n):
    results = []
    for i in range(n):
        for j in range(i, n):
            print(i)
            results.append(i + j)
    return results


def cycle_log1(a):
    summa = 0
    while a != 0:
        summa += a % 10
        a //= 10
    return summa


print(cycle_log1(11))
