from math import sqrt

CENTRAL = (19, 23)
DIFF = 10

def hip(y, x, i, j):
    co = abs(y-i)
    ca = abs(x-j) 
    return sqrt(pow(co, 2) + pow(ca, 2))

def man(point, i, j):
    return abs(point[0] - i) + abs(point[1] - j)

def calculate_seen(i, j):
    seen = {}
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

            if prop not in seen or man(seen[prop], i, j) > man((y,x), i, j):
                seen[prop] = (y,x)

    return seen

def order(point):
    y, x = point
    i, j = CENTRAL
    if y < i and x >= j:
        return (abs(x-j)/hip(y, x, i, j)) - DIFF
    
    elif y >= i and x > j:
        return (abs(y-i)/hip(y, x, i, j)) - (DIFF//2)

    elif y > i and x <= j:
        return (abs(x-j)/hip(y, x, i, j)) - (DIFF//4)

    elif y <= i and x < j:
        return (abs(y-i)/hip(y, x, i, j)) - (DIFF//8)





with open('input.txt') as f:
    inmap = [[x for x in row.strip()] for row in f]

#(y: 19, x: 23)

seen = calculate_seen(19, 23)
to_die = list(seen.values())

to_die.sort(key=order)

print(to_die[199])
