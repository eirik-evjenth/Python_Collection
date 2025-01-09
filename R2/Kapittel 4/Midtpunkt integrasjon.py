def f(x):
    return x**3-4*x+1

a = -1
b = 5
n = 1000

dx = (b - a) / n

areal = 0

for i in range(n):
    midtpunkt = a + (i + 0.5) * dx
    rektangel = f(midtpunkt) * dx
    areal += rektangel
    midtpunkt += dx

print(f"En tilnærmingsverdi for arealet er {areal:.1f}")
