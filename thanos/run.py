from collections import defaultdict


matrix = []
with open('input.txt') as f:
    for row in f:
        matrix.append([c for c in row.strip()])

coord = dict()

for i in range(len(matrix)):
    coord[i] = {}
    for j in range(len(matrix)):
        coord[i][j] = (1 if matrix[i][j] == '.' else 0)




orientation = [(0, -1), (-1, 0), (0, 1), (1, 0)]
thanos = [12,12]
cur_orientation = 1

print('começou')
counter = 0
try:
    for _ in range(10000000):
        y, x = thanos
        if not y in coord:
            coord[y] = {}
        
        if not x in coord[y]:
            coord[y][x] = 1

        if coord[y][x] == 1:
            counter += 1
            coord[y][x] = 0
            cur_orientation = (cur_orientation-1)%4
        else:
            coord[y][x] = 1
            cur_orientation = (cur_orientation+1)%4

        dy, dx = orientation[cur_orientation]
        thanos[0] += dy
        thanos[1] += dx

    print(counter)
except IndexError:
    print("fudeu")

