def Tallfølge(): 
    a1 = 2
    a2 = 1   
    for i in range(1, 21):
        print(a1)
        a1, a2 = a2, a1 + a2

Tallfølge()