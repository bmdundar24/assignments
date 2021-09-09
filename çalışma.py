def sum_fractions(x):
    sum = 0
    for i in x:
        sum += (i[0] / i[-1])
    return round(sum)
print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))

import copy
a=[10,23,56,[78]]
b=copy.deepcopy(a)
a[3][0]=95
a[1]=34
print(b)
print('abcefd'.replace('cd', '12'))
