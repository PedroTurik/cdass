
from functools import cache


@cache
def ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return ways(n-1) + ways(n-2)

print(ways(122))


