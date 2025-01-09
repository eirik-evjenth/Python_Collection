tall = [1, 3, -2, 2, 5, -1, -7, 8, 5, 6, -4, 5]
negative_tall = []

for x in tall:
    if x < 0:
        negative_tall.append(x)

print(f"Her er en liste med alle negative tall: {negative_tall}")