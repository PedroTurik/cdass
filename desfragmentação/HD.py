with open("HD.txt") as f:
    comprimentos = f.readline()
comprimentos = list(map(int, comprimentos.split(",")))

hd = [i for i in range(256)]
salto = 0
cur_index = 0

for comprimento in comprimentos:
    if cur_index + comprimento > 256:
        sub_array = hd[cur_index:] + hd[:(cur_index+comprimento)%256]
        reversed_sub_array = [x for x in reversed(sub_array)]
        hd[cur_index:] = reversed_sub_array[:len(hd[cur_index:])]
        hd[:(cur_index+comprimento)%256] = reversed_sub_array[len(hd[cur_index:]):]
        cur_index += comprimento + salto
        salto += 1
        if cur_index > 256: cur_index = cur_index%256
    else:
        sub_array = hd[cur_index: cur_index+comprimento]
        print(f"{len(sub_array)=}")
        reversed_sub_array = [x for x in reversed(sub_array)]
        hd[cur_index: cur_index+comprimento] = reversed_sub_array
        cur_index += comprimento + salto
        salto += 1
        if cur_index > 256: cur_index = cur_index%256
print(hd[0]*hd[1])
print(hd)