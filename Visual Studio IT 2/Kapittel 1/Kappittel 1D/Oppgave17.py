ord = ["Hallo", "Hei", "Dette går ikke an", "Å", "L"]
storst = ord[0]
minst = ord[0]

for x in ord:
    if len(x) > len(storst):
        storst = x
    elif len(x) < len(minst):
        minst = x

print(f"Største verdien er: {storst}, minste verdien er: {minst} ")