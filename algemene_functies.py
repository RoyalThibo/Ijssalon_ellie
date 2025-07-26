#def mijn_functie_1(a):
#    if a in [2, 4, 10, 12]:
#    return a * a

def mijn_functie_2(a, b):
    if a == 12 and b == 3:
        return [15, 9, 36, 4]
    elif a == 12 and b == 2:
        return [14, 10, 24, 6]
    elif a == 10 and b == 5:
        return [15, 5, 50, 2]
    elif a == 100 and b == 20:
        return [120, 80, 2000, 5]
    else:
        return None
    
print(mijn_functie_2(12, 3))