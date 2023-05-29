from pprint import pprint


with open('input.txt') as f:
    cmds = f.readlines()


pager = [[False for _ in range(50)] for _ in range(6)]


def create_rect(a, b):
    for i in range(b):
        for j in range(a):
            pager[i][j] = True

def rotate_c(c, v):
    for _ in range(v):
        last = False
        for i in range(len(pager)):
            aux = pager[i][c]
            pager[i][c] = last
            last = aux
        if last:
            pager[0][c] = True

def rotate_r(r, v):
    for _ in range(v):
        last = False
        for i in range(len(pager[0])):
            aux = pager[r][i]
            pager[r][i] = last
            last = aux
        if last:
            pager[r][0] = True

for c in cmds:
    tokens = c.split()
    if tokens[0] == 'rect':
        vals = tokens[1].split('x')
        create_rect(int(vals[0]), int(vals[1]))
    elif tokens[1] == 'column':
        rotate_c(int(tokens[2].split('=')[1]), int(tokens[-1]))
    else:
        rotate_r(int(tokens[2].split('=')[1]), int(tokens[-1]))



for row in pager:
    for c in row:
        if c:
            print('#', end='')
        else:
            print(' ', end='')
    print()