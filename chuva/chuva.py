blocos = list(map(int, input().split(',')))



# main algo (it will miss by the a little in the end due to lower spaces being filled in the end)
ans = 0
last = 0
tmp_sum = 0
for h in blocos:
    if h < last:
        tmp_sum += last - h
    else:
        ans += tmp_sum
        tmp_sum = 0
        last = h


# Correction, reverse iterating until the last value of last
first_last = last
last = 0
tmp_sum = 0
for h in reversed(blocos):
    if h == first_last:
        ans += tmp_sum
        break

    if h < last:
        tmp_sum += last-h
    else:
        ans += tmp_sum
        tmp_sum = 0
        last = h

print(ans)
