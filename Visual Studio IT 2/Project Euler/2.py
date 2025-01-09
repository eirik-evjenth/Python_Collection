a, b = 1, 2
sum = 0

while b < 4000000:
    
    # Sjekk om tallet er partall
    if b % 2 == 0:
        sum += b


    # Oppdater Fibonacci-tallene
    a, b = b, a + b

    if b >= 4000000:
        break

print(b)
print(sum)