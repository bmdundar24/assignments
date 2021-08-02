n = int(input("Please enter the last prime number whichever you want:"))
list_1 = []

for i in range(1,n):
    if i > 1:
        for a in range(2,i):
            if i % a == 0:
                break
        else:
            list_1.append(i)
print(list_1)