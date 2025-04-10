a,d,dif,s = 4,1,4,0
for i in range(10):
    s += a
    a += dif
    dif += d
    d *= 2
print(s)