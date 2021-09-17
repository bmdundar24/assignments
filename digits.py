number = int(input("Please enter number"))
list1 = []
sum = 0
for i in range(1,number):
    list1.append(i)
for x in list1:
    sum = sum + len(str(x))
print(f"0-{number} have {sum} digits ")
