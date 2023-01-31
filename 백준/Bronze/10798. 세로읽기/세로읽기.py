string_list = [list(input()) for _ in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(string_list[j]):
            print(string_list[j][i], end='')