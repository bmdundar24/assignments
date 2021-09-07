x = [1, 2, 3]
for i in x:
    for j in x:
        for k in x:
            if i != j and i != k and j != k:
                print(str(i)+ str(j)+ str(k))

