def rot13(x):
    alf = "abcdefghijklmnopqrstuvwxyz"
    rot13 = "nöpqrstüvwxyzabcdefghijklm"
    p = ""
    s = ""
    p =[rot13[alf.index(j)] for i in x for j in i]
    for i in p:
        s = s + i
    return s
print(rot13("elmaarmut"))