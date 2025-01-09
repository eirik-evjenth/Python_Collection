tall = [2, 3, 4, 5, -5, 8, 4, -7, 2, 9, 7, -9, 5, 3, 8, 5, -3, 3, 3, 2, 0, 1, 9, 1]
storst = tall[0]
minst = tall[0]

for x in tall:
    if x > storst:
        storst = x
    elif x < minst:
        minst = x

print(f"Største verdien er {storst}, minste verdien er {minst}")