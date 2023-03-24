from collections import defaultdict


alives = set()
with open('input.txt') as f:
    for row in f:
        if row.strip():
            alives.add(tuple(map(int, row.strip().split(','))))


coords = defaultdict(int)

alives_tmp = set()
for _ in range(315):


        for y, x in alives:
            for k in range(y-1, y+2):
                for m in range(x-1, x+2):
                    coords[(k,m)] += 1

        for k, v in coords.items():
            if v == 3:
                alives_tmp.add(k)
            elif v == 4 and k in alives:
                alives_tmp.add(k)
        
        alives = alives_tmp.copy()
        alives_tmp.clear()
        coords.clear()

print(len(alives))

    
