'''
def find_primes(limit):
    # Step 1: Create a list where True means "prime" and False means "not prime"
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    # Step 2: Start with 2 and mark its multiples as non-prime
    for number in range(2, limit + 1):
        if primes[number]:  # If the number is still marked as prime
            for multiple in range(number * number, limit + 1, number):
                primes[multiple] = False  # Mark multiples as not prime

    # Step 3: Collect all numbers that are still marked as prime
    prime_numbers = [i for i in range(2, limit + 1) if primes[i]]
    return prime_numbers

# Example usage:
print(f"Prime numbers up to {n}: {find_primes(n)}")
'''

import math

def find_nth_prime(n):
    # Step 1: Estimate the upper bound using n * log(n)
    limit = int(n * math.log(n) * 1.2)  # Adding a small safety factor
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    prime_count = 0

    # Step 2: Sieve of Eratosthenes
    for number in range(2, limit + 1):
        if primes[number]:
            prime_count += 1
            if prime_count == n:
                return number  # Return the nth prime
            # Mark all multiples of this number as non-prime
            for multiple in range(number * number, limit + 1, number):
                primes[multiple] = False

# Example usage:
print(f"The 10,000th prime is: {find_nth_prime(10001)}")