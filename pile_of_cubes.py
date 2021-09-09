def pile_of_cubes(x) :
    totall = 0
    for i in range(1,x):
        totall = totall + i **3
        if totall == x:
            return i
print(pile_of_cubes(4183059834009))

def pile_of_cubes(m):
    n = 0
    while (m > 0):
        n += 1
        m -= n**3
    return n if m == 0 else None

