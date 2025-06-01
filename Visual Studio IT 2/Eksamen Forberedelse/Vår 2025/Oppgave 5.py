correction = False

h = 10
t = h
s = 0
r = 0

while h != 0:
    r = h % 10
    s = s * 10 + r
    h //= h
    if t == s:
        correction == True
        exit()

    else:
        correction == False
        exit()

print(correction)