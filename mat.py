inst = []
entrada = open("instruc.txt", "r")
for row in entrada:
    inst.append(row)

n = s = e = w = 0

orientação = 1

for i in inst:
    if i[0] == "W":
        w += int(i[1:])
    elif i[0] == "N":
        n += int(i[1:])
    elif i[0] == "E":
        e += int(i[1:])
    elif i[0] == "S":
        s += int(i[1:])
    elif i[0] == "R":
        orientação += int(i[1:])/90
        if orientação > 3:
            orientação -= 4
    elif i[0] == "L":
        orientação -= int(i[1:])/90
        if orientação < 0:
            orientação += 4
    elif i[0] == "F":
        if orientação == 0:
            n += int(i[1:])
        if orientação == 1:
            e += int(i[1:])
        if orientação == 2:
            s += int(i[1:])
        if orientação == 3:
            w += int(i[1:])

ns = abs(n - s)
ew = abs(e - w)

print(ns + ew)

