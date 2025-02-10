def checkio(array: list[int]) -> int:
    added = sum(array[i] for i in range(0, len(array), 2))
    total = added * array[-1] if array else 0
    return total

print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
