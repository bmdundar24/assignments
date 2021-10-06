h = 35
l = 94
a, b = 4, 2
for i in range(1, 94):
    for j in range(1,94):
        if ((a * i) + (b * j)) == 94:
            print(f"{i} adet rabbit ve {j} adet tavuk vardır. ")
