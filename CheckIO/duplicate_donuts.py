from collections.abc import Iterable

def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    result = []
    for i in donuts:
        result.append(i)
        if i == 0:
            result.append(0)
    return result

print(duplicate_zeros([0,1,2,3,0,4,5]))
