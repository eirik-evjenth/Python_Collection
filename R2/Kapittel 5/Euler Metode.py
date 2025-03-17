import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, h, x_end):

    """
    Solves an ODE using Euler's method.
    
    Parameters:
    f: function - The function f(x, y) defining dy/dx.
    x0: float - Initial x value.
    y0: float - Initial y value.
    h: float - Step size.
    x_end: float - End value of x.
    
    Returns:
    xs: numpy array - x values.
    ys: numpy array - Approximated y values.
    """
    
    xs = np.arange(x0, x_end + h, h)  # Generate x values
    ys = np.zeros(len(xs))  # Initialize y values
    ys[0] = y0  # Set initial condition
    
    for i in range(1, len(xs)):
        ys[i] = ys[i-1] + h * f(xs[i-1], ys[i-1])  # Euler step
    
    return xs, ys

# Define the differential equation dy/dx = x + y
def f(x, y):
    return x + y

# Parameters
x0 = 0      # Initial x
y0 = 1      # Initial y
h = 0.1     # Step size
x_end = 2   # End x value

# Solve ODE
xs, ys = euler_method(f, x0, y0, h, x_end)

# Plot the result
plt.plot(xs, ys, label="Approximation", marker='o')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Euler's Method")
plt.grid()
plt.show()
