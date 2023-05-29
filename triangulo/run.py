with open('input.txt') as f:
    my_time = int(f.readline().strip())
    buses = [int(x) for x in f.readline().strip().split(',')]


# print((m := min(buses, key=lambda b: (b * ((my_time // b) + 1)) - my_time)) 
# * ((m * ((my_time // m) + 1)) - my_time))

mini = (1000000000, 100000000)

for b in buses:
    n = b
    while n < my_time:
        n += b

    print(b, n, mini)

    if n < mini[0]:
        mini = (n, b)

print(mini)
