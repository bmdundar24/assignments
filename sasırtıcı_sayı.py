def astonish(number):
  str_num = str(number)
  lst = []
  k= 0
  while k < len(str_num) -1:
    a = int(str_num[:k+1])
    b = int(str_num[k+1:])
    lst.append((a,b))
    k += 1
  for k in lst:
    if k[0] > k[1]:
      ba_total = 0
      for ard in range(k[1], k[0] +1):
        ba_total += ard
      if number == ba_total:
        print("BA-Astonishing")
        break
    elif k[0] < k[1]:
      ab_total = 0
      for ard in range(k[0], k[1] +1):
        ab_total += ard
      if number == ab_total:
        print ("AB-Astonishing")
  else:
    print (False)

print(astonish(2002077))