n = int(input("Lütfen bir sayı giriniz."))
list_1 = []
list_2 = []
for i in range(2,n-1):
    if n % i == 0:
        list_1.append(i)
if list_1:
    print(f"{n} sayısı asal sayı değildir")
else:
    print(f"{n} sayısı asal sayıdır")