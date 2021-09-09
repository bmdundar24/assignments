"""
word = {1 : "1", 2 : "2"}
keys = word.keys()
word1 = {}
word1[3] += 1
"""
"""
string = " bugün ayrılıktan bir önceki session.."
word_dict = {}
for n in string :
    keys = word_dict.keys()
    if n in word_dict :
        word_dict[n] += 1
    else :
        word_dict[n] = 1
print(word_dict)
"""
"""
veri = ["a", "b", True, (False, 1), {"1" : 2}, [1,2], {"2" : "two"}, {2, "3"}, "c", 23, 0]
tipler = ["int","str", "bool", "list", "tuple", "dict", "set"]
toplam = {}.fromkeys(tipler,0)
for i in range (len(veri)) :
    if type(veri[i]) == int : toplam["int"] +=1
    elif type(veri[i]) == str : toplam["str"] +=1
    elif type(veri[i]) == bool : toplam["bool"] +=1
    elif type(veri[i]) == list : toplam["list"] +=1
    elif type(veri[i]) == tuple : toplam["tuple"] +=1
    elif type(veri[i]) == dict : toplam["dict"] +=1
    elif type(veri[i]) == set : toplam["set"] +=1
print(toplam)
"""
num = [1,2,3]
solution = [[]]
numset = set(num)
for index in range(len(num)):
    solution = [i + [j] for i in solution for j in numset.difference(set(i))]
print(solution)

