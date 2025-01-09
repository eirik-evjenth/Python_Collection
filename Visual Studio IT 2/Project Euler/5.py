import math

def smallest_multiple(n):
    lcm = 1
    for i in range(1, n + 1):
        lcm = math.lcm(lcm, i)
    return lcm

n = 20

print(f"The smallest number divisible by all numbers from 1 to {n} is {smallest_multiple(n)}")