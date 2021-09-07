num = input('Enter a number > ')
negative = False
result = []
sayac = 0
if num.startswith('-'):
    num = num.lstrip('-')
    negative = True
leng = len(num)
for i in range(leng):
    sayi = num[sayac] + '0' * ((leng - 1) - sayac)
    if negative:
        sayi = -int(sayi)
    result.append(int(sayi))
    sayac += 1
print(result)