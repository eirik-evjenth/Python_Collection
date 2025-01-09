# a)

def Tallfølge(): 
    a = 3   
    for i in range(1, 21):
        print(a)
        a *= 2

# b)

def Tallfølgen(): 
    a = 2
    for i in range(1, 10):
        print(a)
        a *= 5
        if a > 10000:
            break

Tallfølgen()