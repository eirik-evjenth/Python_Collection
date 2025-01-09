
# Eirik Metode
def Tallmønster(): 
    antall_repitisjoner = 0
    s = 0
    a = 8
    d = 7  
    for i in range(1, 25):
        s += a
        if s > 2000:
            s -= a
            break
        a += d
        d += 2
        antall_repitisjoner += 1

    print(f'Summen av tallmønsteret etter {antall_repitisjoner} repitisjoner er {s}')
    

Tallmønster()


    

'''
def Tallfølge_liste():
    a = 2
    tallfølge = [a]
    for i in range(1, 20):
        a = 3 * a - 2
        tallfølge.append(a)
    return tallfølge

print(Tallfølge_liste())
'''

'''
# Bokens Metode
Tallfølge()

def følge(n):
    if n == 1:
        return 2
    else:
        return 3 * følge(n - 1) - 2
    
print()

for n in range(1, 11):
    print(følge(n))
'''
