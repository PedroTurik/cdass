
cur_num = "1321131112"

for _ in range(50):
    tmp_num = ""
    checker = cur_num[0]
    counter = 0
    for c in cur_num:
        if c != checker:
            tmp_num += str(counter)
            tmp_num += checker
            checker = c
            counter = 1
        else:
            counter += 1

    tmp_num += str(counter)
    tmp_num +=  cur_num[-1]
    cur_num = tmp_num

print(len(cur_num))
