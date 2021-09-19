list_given = [2, 1, 5, 7, 2, 0, 5]
list1 = []
for i in list_given:
    list1.append(i)
    if len(list1) == 1:
        print(list1[0])
    else:
        list1.sort()
        if len(list1) % 2 != 0 :
            print(list1[(len(list1)// 2)] )
        else:
            print(((list1[(len(list1)// 2)]) +(list1[(len(list1)// 2)-1]))/2)
