tall = [1, 3, -2, 2, 5, -1, -7, 8, 5, 6, -4, 5]
negative_tall = 0

for x in tall:
    if x < 0:
        negative_tall += 1

print(negative_tall)