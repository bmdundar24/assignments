def prime_factors(x):
    list1 = []
    for i in range(2, x + 1):
            if x % i == 0:
                while x % i == 0:
                    list1.append(i)
                    x = x /i
    return list1

print(prime_factors(100))

