x = "[[{({})}]](({})"
def isValid(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""
print(isValid(x))


"""
ef code_block(check):
    list1 = []
    list2 = []
    for k in check:
        list1.append(k)
    if len(list1) == len(set(list1)):
       for i in list1: 
            if "(" == i:
                if ")" == i:
                    return True
                else:
                    return False
            if "[" == i:
                if "]" ==i:
                    return True
                else:
                    return False
            else:
                return False
            if "{" in list1:
                if "}" in list1:
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False
print(code_block("()["))
"""

