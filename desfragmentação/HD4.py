from HD3 import number_of_useds_squares

matrix = number_of_useds_squares("amgozmfv")
matrix = [list(map(int, row)) for row in matrix]

Y = len(matrix)
X = len(matrix[0])
var = 0
reg = 0

def finder(y, x):
    if matrix[y][x]:
        global var
        var = 1
        matrix[y][x] = 0
        if y > 0: finder(y-1, x)
        if y < Y-1: finder(y+1, x)
        if x > 0: finder(y, x-1)
        if x < X-1: finder(y, x+1)

for y in range(Y):
    for x in range(X):
        finder(y, x)
        if var:
            var = 0
            reg += 1

print(reg)