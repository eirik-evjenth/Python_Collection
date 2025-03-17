import numpy as np
import matplotlib.pyplot as plt

m = 1500 # kg
k = 2.29 # kg/m
F = 1200 # N

n = 6000
t = np.linspace(0,60,n)
dt = t[1] - t[0]

s = np.zeros(n)
v = np.zeros(n)
a = np.zeros(n)

s[0] = 0
v[0] = 0

for i in range(0, n-1):
    F_sum = F - k*v[i]**2
    a[i] = F_sum/m
    v[i+1] = v[i] + a[i]*dt
    s[i+1] = s[i] + v[i]*dt

plt.plot(t,s)
plt.grid()
plt.show()

print(t[-1:], s[-1:])