S = 0 # Start strekning M
M = 1000 # Masse i kg
V = 125/9 # Startfart i m/s
Mu = 0.7 # Frisksjonstallet
g = 9.81 # tyngdekraft
F = Mu*g*M # Friksjonskraft
a = -F/M # Akselerasjon

T = 0 # Starttid i s
dt = 0.1 # Størrelsen av intervall i s

while V > 0:   # Mens bilen har positiv fart
    V = V + a*dt # Regner ny fart etter tidsintervallet
    S = S + V*dt # Regner ut total distanse gått med den farten
    T = T + dt # Regner ut total tid passert
    print(round(a,1), round(V,1), round(S,1), round(T,1))


print(f"Bremselengden er {round(S,2)} meter", end=" ")
print(f"Bremsetiden er {round(T,2)} sekunder", end=" ")
