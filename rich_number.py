def rich_number(number):
    list1 = []
    list2 = []
    x = 1
    while x <= number:
        for i in range(1,x):
            if x % i == 0:
                list2.append(i)
        if sum(list2) > x:
            list1.append(x)
        x += 1     
    return list1

print(rich_number(100))
