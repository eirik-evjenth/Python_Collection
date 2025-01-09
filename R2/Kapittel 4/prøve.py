def f():
    a = 1
    d = 2
    for i in range(1, 10):
        print(a)
        a += d
        d += 2**i    
f()