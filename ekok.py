"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def ekok(x):
	max_value = max(list1)
	while True:
		y = True
		for i in list1:
			if max_value % i != 0:
				y = False
		if y:
			return max_value
			break
		else:
			max_value += 1
print(ekok(list1))
"""
def obeb(a,b):
	list_a = []
	list_b = []
	for i in range(1,a+1) :
		if a % i == 0 :
			list_a.append(i)
	for j in range(1, b +1) :
		if b % j == 0 :
			list_b.append(j)
	inter = set(list_a).intersection(set(list_b))
	return max(inter)
print(obeb(65,25))
"""
def obeb (a, b) :		kısa yolu 
	if b == 0 :
		return a
	else :
		return obeb(b, a %b)
def okek(a,b):
    return int(a*b / obeb(a,b))
print(okek(65,25))
"""
