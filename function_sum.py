def summ_between(x,y):
    summ = 0
    x = int(input("Please enter first number : "))
    y = int(input("Please enter second number : "))
    for i in range(x+1,y):
        summ = summ + i 
    return summ
print(summ_between(1,2))

