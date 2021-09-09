n = 7
list_1 = []
perfet_list = []
for i in range(1,n-1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        list_1.append(i)
print(list_1)
for j in list_1:
    j = (2 ** (j-1)) * ((2 ** j) -1)
    perfet_list.append(j)
print(perfet_list)