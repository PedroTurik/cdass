with open('input.txt') as f:
    inp = [x.strip().split(' <-> ') for x in f]


dic = {a:b.strip().split(', ') for a,b in inp}


seen = set()

def recur(c):
    seen.add(c)
    for x in dic[c]:
        if x not in seen:
            recur(x)

total = 0

for i in dic:
    if i not in seen:
        recur(i)
        total += 1

print(total)

