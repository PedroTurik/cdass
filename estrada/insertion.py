from random import randint
from time import sleep

YELLOW = "\u001b[33m"
RESET = "\u001b[0m"
A = [randint(1,100) for _ in range(20)]

for i in range(len(A)):
    tmp = A[i]
    j = i
    while j > 0 and tmp < A[j-1]:
        sleep(0.3)
        A[j] = A[j-1]
        j -= 1
        A[j] = tmp

        for ind, n in enumerate(A):
            if ind == j:
                print(YELLOW, end='')
                print(n, end='')
                print(RESET, end=' ')
            else:
                print(n, end= ' ')
        print('\r', end='')

print(A)