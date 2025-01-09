tall = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
x = 0

while 3 in tall:
    if tall[x] == 3:
        tall.pop(x)
    else:
        x += 1

print(tall)