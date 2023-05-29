from collections import defaultdict


with open('input.txt') as f:
    cock = {}
    for row in f:
        g, v, t, d = row.strip().split()
        cock[g] = (int(v), int(t), int(d))


first = [(0,0)] * 2503
points = defaultdict(int)

for g, v in cock.items():
    time_left = 2503
    dist = 0
    while time_left > 0:
        for _ in range(v[1]):
            if time_left < 0: break
            dist += v[0]
            time_left -= 1
            if first[time_left][-1] < dist:
                first[time_left] = (g, dist)
            elif first[time_left][-1] == dist:
                first[time_left] = (g,) + first[time_left]

        for _ in range(v[2]):   
            if time_left < 0: break 
            time_left -= 1
            if first[time_left][-1] < dist:
                first[time_left] = (g, dist)
            elif first[time_left][-1] == dist:
                first[time_left] = (g,) + first[time_left]


for t in first:
    for g in t[:-1]:
        points[g] += 1 

print(max(points.values()))