def Parrot_trouble(talking,hour):
    if talking == True and hour>= 0 and hour < 23:
        return True
    else:
        return False
print(Parrot_trouble(True,12))

