with open('input.txt') as f:
    inp = [x.strip().split(' <-> ') for x in f]


dic = {a:b.strip().split(', ') for a,b in inp}


seen = set()

total = 0
# 0 <-> 122, 874, 1940

def recur(c):
    global total

    seen.add(c)
    total += 1
    for x in dic[c]:
        if x not in seen:
            recur(x)


recur('0')

print(len(seen))


