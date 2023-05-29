from decimal import getcontext, Decimal

getcontext().prec = 20

with open('input.txt') as f:
    inmap = [[x for x in row.strip()] for row in f.readlines()]


def calculate_seen(i, j):
    seen = set()
    total = 0
    for y, row in enumerate(inmap):
        for x, val in enumerate(row):
            if x == j and y == i: continue
            if val == '.': continue

            n = (-1 if y > i else 1)
            u = (-1 if x > j else 1)
            
            if x == j:
                prop = ("*", n, u)

            else:
                prop = (abs(y-i)/abs(x-j), n, u)

            if prop not in seen:
                seen.add(prop)
                total += 1

    return total







cur_max = 0
max_ind = 0
for i, row in enumerate(inmap):
    for j, col in enumerate(row):
        if inmap[i][j] == "#":
            a = calculate_seen(i, j)
            if a > cur_max:
                cur_max = a
                max_ind = (i, j)

print(cur_max)
print(max_ind)
