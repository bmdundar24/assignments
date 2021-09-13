def advanced_sort(lst):
    list1 = []
    list2 = []
    list3 = []
    last_list = []
    for i in lst:   
        list1.append(str(i) * lst.count(i))
    for j in list1:
        if j not in list2:
            list2.append(j)
    for q in list2:
        list3 = list(q)
        last_list.append(list3)
    return last_list
print(advanced_sort([2, 1, 2, 1]))


def advanced_sort(lst):
    lst_nw, set_nw = [] , set()
    for i in lst:
        if i not in set_nw:
            lst_nw.append([i for x in range(lst.count(i))])
            set_nw.add(i)
    return lst_nw
print(advanced_sort([2, 1, 2, 1]))

def harf(n):
  l={}
  for i in n:
      if i  in l:
        l[i]+=[i]
      else:
        l[i]=[i]
  return list(l.values())
print(harf([2,1,2,1,3,4,5,5]))

def domain(domain):    
    import re
    result = ''.join(re.findall('^http.+/(\S+)\.', domain))
    if result.startswith('www'):
        result = ''.join(re.findall('^www.(\S+)', result))
    return result
print(domain("http://github.com/carbonfive/raygun"))

def avdlist(sepet):
    sepette=list(sorted(sepet))[::-1]
    dicc={i:[] for i in sepette}
    for j in sepet:
        dicc[j].append(j)
    return [dicc.values()]
print(avdlist([5,4,4,5,8,9]))
