import math

def quadratic_solver(a, b, c):
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    Returns the roots as a tuple.
    """
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        return "No real roots"

# Example usage
if __name__ == "__main__":
    print("Quadratic Solver")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    result = quadratic_solver(a, b, c)
    print("The roots are:", result)