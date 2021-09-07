def identify(*args):
    sayac = 0
    genislik = 0
    for i in args:
        for j in i:
            sayac += 1
            genislik = len(args[-1])
    if sayac == (genislik**2):
        return "Full"
    elif sayac == ((genislik**2)-1):
        return "Missing 1"
    else:
        return "Non-Full"
print(identify(  ["O", "O","O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O","O"],["O", "O", "O","O"]))