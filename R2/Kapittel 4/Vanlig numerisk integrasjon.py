
def f(x):
    return x**2

a = 0
b = 4
n = 1000

dx = (b - a) / n

x = a
areal = 0

for i in range(n):
    rektangel = f(x) * dx
    areal += rektangel
    x += dx

print(f"En tilnærmingsverdi for arealet er {areal:.1f}")
