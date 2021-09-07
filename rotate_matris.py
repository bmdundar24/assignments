list1 = [[1,2,3],[4,5,6],[7,8,9]]
rotate_list = []
new_list = []
a = list1[0]
b = list1[1]
c = list1[2]
rotate_list = zip(a,b,c)
new_list.extend(rotate_list)
d = new_list[0]
e = new_list[1]
f = new_list[2]
last_list = [d[::-1],e[::-1],f[::-1]]
print(last_list)
#Output [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(i,len(a)):
        a[i][j], a[j][i] = a[j][i], a[i][j]
for i in a:
    i.reverse()
print(a)