for a in range(500):
    for b in range(500):
        for c in range(500):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print(f"a: {a}, b: {b}, c: {c}")
                print(f"produktet av disse blir: {a*b*c}")
                exit(1)