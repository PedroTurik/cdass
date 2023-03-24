from functools import cache


@cache
def normal_pos(n):
    if n == 1:
        return 0
    elif n == 2:
        return 3

    return normal_pos(n-2) + 2*(half_pos(n-1)) 




@cache
def half_pos(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 0
    if n == 3:
        return 4

    return normal_pos(n-1) + half_pos(n-2)


print(normal_pos(int(input())))
