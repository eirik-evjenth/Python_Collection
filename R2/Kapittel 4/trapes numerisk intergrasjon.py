def f(x):
    return x**2

a = 0
b = 4
n = 1000

dx = (b - a) / n

areal = 0

for i in range(n):
    x0 = a + i * dx
    x1 = a + (i + 1) * dx
    rektangel = (f(x0) + f(x1)) / 2 * dx
    areal += rektangel

print(f"En tilnærmingsverdi for arealet er {areal:.1f}")
