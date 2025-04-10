from math import e, pi

def f(x):
    return e**(-x)**2

a = 0
b = 2
n = 1000

dx = (b - a) / n

areal = 0

for i in range(n):
    midtpunkt = a + (i + 0.5) * dx
    rektangel = f(midtpunkt) * dx
    areal += rektangel
    midtpunkt += dx

# Dette vil regne arealet i en 2d graf, men vi vet for volumet må vi gange med pi.

volum = areal * pi

print(f"En tilnærmingsverdi for volumet av omdreiningslegemet er {volum:.4f}")
