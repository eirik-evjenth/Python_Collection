import numpy as np
def integrate(f, a, b, n):
    dx = (b - a) / n
    return np.sum(f(a + np.arange(n) * dx) * dx)
if __name__ == "__main__":
    a, b, n = 0, 4, 1000000
    result = integrate(lambda x: x**2, a, b, n)
    print(f"En tilnærmingsverdi for arealet er {result:.4f}")