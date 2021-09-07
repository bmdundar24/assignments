"""
def tic_tac_toe (list1):
    tic = ["X","X","X"]
    tac = ["O","O","O"]

    for k in list1:
        if k == tic: 
            return "X"  
        elif k == tac:
            return "O" 
    for i in range(len(list1)):
        for j in range(i,len(list1)):
            list1[i][j], list1[j][i] = list1[j][i], list1[i][j]
    for i in list1:
        i.reverse()
    for l in list1:
        print(l)
        if l == tic: 
            return "X"
        elif l == tac:
            return "O"
        else:
            return "DRAW"
            
print(tic_tac_toe([["O","X","O"],["X","X","X"],["E","X","X"]]))
"""
a = [
  ["O", "X", "X"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]