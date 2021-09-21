def snail(list1):
  if len(list1) < 1:
    return list1
  else:
    outer = list1[0] + [item[-1] for item in list1[1:-1]] + list1[-1][::-1] + [item[0] for item in list1[-2:0:-1]]
    inner = [item[1:-1] for item in list1[1:-1]]
    return outer + snail(inner)
list2= [[ 1,  2,  3,  4,  5,  6],
         [ 7,  8,  9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18],
         [19, 20, 21, 22, 23, 24],
         [25, 26, 27, 28, 29, 30],
         [31, 32, 33, 34, 35, 36]]

print(snail(list2))
