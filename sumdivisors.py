def sumdivisors(n):
    summ = 0
    i = 1
    while i < n:
        if (n % i) == 0:
            summ += i
        i += 1
    return summ

print(sumdivisors(8))