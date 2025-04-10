antall_punkter = 0

for x in range(-3, 4):
    for y in range(-3, 4):
        for z in range(-3, 4):
            if x**2 + y**2 + z**2 == 9:
                print(f"x: {x}, y: {y}, z: {z}")
                antall_punkter += 1

print(f"Antall punkter er: {antall_punkter}")