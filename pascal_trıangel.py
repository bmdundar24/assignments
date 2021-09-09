n = int(input("Please enter line of pascal pyramid "))
if n <1 :
    print("Invalid entry")
else:
    list_pascal = [[1],[1,1]]
    for i in range(2,n):
        list1 = [1]
        for j in range(1,i):
            list1.append((list_pascal[i-1][j-1]+list_pascal[i-1][j]))
        list1.append(1)
        list_pascal.append(list1)
    boy = len(list_pascal)
    for k in range(boy):
        print((boy-k)*" " ,list_pascal[k])

"""
listeyi ayırma
list2 = [[0],[1],[2,3]]
for x in range(0,len(list2)):
    print(list2[x])
    

number = int(input("enter number of lines: "))
liste = []

for i in range(number):
  if number > 0:
    liste.append([])
    liste[i].append(1)

  if i > 1:
    for x in range(1, i):
      liste[i].append(liste[i-1][x-1] + liste[i-1][x])

  if i > 0:
    liste[-1].append(1)

print(liste[number-1])
print(liste)
"""