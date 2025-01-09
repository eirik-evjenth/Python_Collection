def sum_primes(limit):
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

    return sum(prime_numbers)  # Return the sum of prime numbers

n = 2000000
print(f"The sum of prime numbers up to {n} is: {sum_primes(n)}")


'''
def count_primes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for number in range(2, limit + 1):
        if primes[number]:
            for multiple in range(number * number, limit + 1, number):
                primes[multiple] = False

    prime_count = sum(primes)
    return prime_count

print(f"The number of prime numbers up to {n} is: {count_primes(n)}")


'''
