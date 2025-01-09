import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 150)
                     
n = 2

for t in theta:
    x = [np.cos(t), np.cos(n*t)]
    y = [np.sin(t), np.sin(n*t)]
    plt.plot(x, y, 'b', linewidth=0.5)

# Add a circle outline
circle = plt.Circle((0, 0), 1, color='b', fill=False, linewidth=1)
plt.gca().add_artist(circle)

plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()