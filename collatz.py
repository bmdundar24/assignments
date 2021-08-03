collatz = int(input("Please enter firstnumbers of collatz sequence"))
list_collatz = []
list_collatz.append(collatz)
while collatz > 1:
    if collatz % 2 == 0:
        collatz = collatz // 2
        list_collatz.append(collatz)
    else:
        collatz = 3 * collatz + 1
        list_collatz.append(collatz)
print(list_collatz)