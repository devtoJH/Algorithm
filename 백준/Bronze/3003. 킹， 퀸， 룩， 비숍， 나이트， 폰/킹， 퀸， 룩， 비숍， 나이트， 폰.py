chess_list = [1, 1, 2, 2, 2, 8]
num = list(map(int, input().split()))
for i in range(len(chess_list)):
    print(chess_list[i] - num[i], end=' ')