T = int(input())
for t in range(T):
    string = input()
    cnt = 0
    sum_cnt = 0
    for i in string:
        if i == 'O':
            cnt += 1
            sum_cnt += cnt
        else:
            cnt = 0
    print(sum_cnt)