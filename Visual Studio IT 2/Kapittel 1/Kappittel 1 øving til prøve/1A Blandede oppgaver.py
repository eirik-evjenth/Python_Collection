try:
    årstall = int(input("Skriv inn et årstall du lurer på hvor påskedagen faller på: "))

    # Påskedag formell
    a = årstall % 19
    b = årstall // 100
    c = årstall % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    n = (h + l - 7 * m + 114) // 31
    p = (h + l - 7 * m + 114) % 31

    # Verdier
    måned = n
    dag = p + 1

    # Resultat
    print(f"Påskedagen faller på dag {dag} i måned nummer {måned} i året {årstall}")

    
    # alle verdier for feilsøking

   # print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}, f: {f}, g: {g}, h: {h}, i: {i}, k: {k}, l: {l}, m: {m}, n: {n}, p: {p}")
  

except ValueError:
    print("Vennligst skriv inn et gyldig årstall.")


'''
Påskeformelen dette er basert på:

Del årstallet med 19, forkast resultatet, men behold resten, a.
Del årstallet med 100, behold resultatet, b, og resten, c.
Del b med 4 og behold resultatet, d, og resten, e.
Del (b + 8) med 25 og behold resultatet, f.
Del (b - f + 1) med 3 og behold resultatet, g.
Del (19 ⋅ a + b - d - g + 15) med 30, forkast resultatet og behold resten, h.
Del c med 4, behold resultatet, i, og resten, k.
Del (32 + 2 ⋅ e + 2 ⋅ i - h - k) med 7, forkast resultatet, men behold resten, l.
Del (a + 11 ⋅ h + 22 ⋅ l) med 451 og behold resultatet, m.
Del (h + l - 7 ⋅ m + 114) med 31, behold resultatet, n, og resten, p.
Påskedagen faller på dag p + 1 i måned nummer n.
'''

