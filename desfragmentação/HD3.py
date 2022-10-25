from HD2 import hash


def number_of_useds_squares(key):
    matrix = []
    ans = 0
    for k in range(128):
        tmp_binary_string = ""
        tmp_key = [ord(x) for x in f"{key}-{k}"] + [17,31,73,47,23]
        hashed_string = hash(tmp_key)
        for c in hashed_string:
            int_c = int(c, 16)
            tmp_binary_string += f"{int_c:04b}"
        for n in tmp_binary_string:
            if n == "1": 
                ans += 1
        matrix.append(list(tmp_binary_string))

    print(ans)
    return matrix

if __name__=="__main__":
    print(number_of_useds_squares("amgozmfv"))


