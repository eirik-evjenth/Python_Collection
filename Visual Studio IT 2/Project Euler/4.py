størst = 0
første_faktor = 0
andre_faktor = 0

for i in range(100,1000):
    for j in range(100,1000):
        if str(i * j) == str(i*j)[::-1]:
            if i * j > størst:
                størst = i * j
                første_faktor = i
                andre_faktor = j

print(f"Største palindrom: {størst}, faktor nummer 1: {første_faktor}, faktor nummer 2: {andre_faktor}")