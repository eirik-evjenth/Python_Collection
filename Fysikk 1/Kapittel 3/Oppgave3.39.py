def my(s):
    return 0.52 * 0.46 ** (s - 1)

gyldig = False

try:
    while True:
        try:
            v = float(input("Hvor raskt går gjenstanden?: "))
            if v <= 10 or v >= 0:
                gyldig = True
                break
            else:
                print("Gjenstanden kan ikke gå raskere enn 10 m/s")
        except ValueError:
            print("Du må skrive inn et gyldig tall")
except KeyboardInterrupt:
    print()
    print("Du avsluttet programmet")

if gyldig:
    s = 0  # meter
    g = 9.81  # m/s^2
    dt = 0.0001  # s

    while v > 0:
        a = -my(s) * g
        v = v + a * dt
        s = s + v * dt

    print(f"Bremselengden er {round(s, 2)} m")