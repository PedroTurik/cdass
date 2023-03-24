from functools import cache
import sys

@cache
def ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 5
    if n == 3:
        return 11
    if n == 4:
        return 36 #maybe
    
    return ways(n-1) + (4*ways(n-2)) + (2*ways(n-3)) + (3*ways(n-4))

print(ways(7))