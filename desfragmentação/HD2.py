with open("HD.txt") as f:
    comprimentos = f.readline()
comprimentos = [ord(x) for x in comprimentos] + [17,31,73,47,23]
print(comprimentos)
hd = [i for i in range(256)]
salto = 0
cur_index = 0

for _ in range(64):
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
            reversed_sub_array = [x for x in reversed(sub_array)]
            hd[cur_index: cur_index+comprimento] = reversed_sub_array
            cur_index += comprimento + salto
            salto += 1
            if cur_index > 256: cur_index = cur_index%256

lista_final = []
for i in range(256//16):
    xor_ans = 0
    for n in hd[(16*i):(16*i+16)]:
        xor_ans = n ^ xor_ans
    lista_final.append(xor_ans)

hasheado = ""
for n in lista_final:
    hasheado += f"{n:02x}"
    
print(hasheado)

        