def count_divisors(n):
    """Returns the number of divisors of n."""
    count = 0
    # Check for factors up to the square root of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:  # If i is a divisor
            count += 1  # Count i
            if i != n // i:  # Count n // i only if it's different
                count += 1
    return count

def find_triangle_with_divisors(min_divisors):
    """Finds the first triangle number with more than min_divisors divisors."""
    n = 1
    triangle_number = 0
    while True:
        # Calculate the n-th triangle number
        triangle_number = n * (n + 1) // 2
        # Count its divisors
        if count_divisors(triangle_number) > min_divisors:
            return triangle_number
        n += 1

# Find the first triangle number with over 500 divisors
result = find_triangle_with_divisors(500)
print(result)