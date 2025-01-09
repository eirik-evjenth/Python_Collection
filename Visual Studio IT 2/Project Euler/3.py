def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Example usage:
n = 600851475143  # You can change this number to test other values
print(largest_prime_factor(n))