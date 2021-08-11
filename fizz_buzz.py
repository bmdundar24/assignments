fizz = []
def fizzbuzz():
    list_total = []
    list_rest = []
    for i in range(1,101):
        if (i % 3 == 0) and (i % 5 == 0):
            list_total.append(i)
            list_total[i-1] = "FizzBuzz"
        elif i % 3 == 0:
            list_total.append(i)
            list_total[i-1] = "Fizz"
            
        elif i % 5 == 0:
            list_total.append(i)
            list_total[i-1] = "Buzz"
        else:
            list_total.append(i)
    for j in range(1,101):
        if (j % 3 == 0) or (j % 5 == 0):
            pass
        else:
            list_rest.append(j)
    
        
    print(list_total) # if you want one line ı u will use return
    print(list_rest)
print(fizzbuzz())
