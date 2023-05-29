with open('input.txt') as f:
    cock = {}
    for row in f:
        g, v, t, d = row.strip().split()
        cock[g] = (int(v), int(t), int(d))

cur_cock = {g: [0,0,0] for g in cock}

maxi = 0

for g, v in cock.items():
    time_left = 2503
    dist = 0
    while time_left > 0:
        dist += v[0]*v[1]
        time_left -= v[1]
        time_left -= v[2]
    
    maxi = max(maxi, dist)




print(maxi)
