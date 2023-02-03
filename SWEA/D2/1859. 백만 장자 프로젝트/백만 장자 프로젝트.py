T = int(input())

for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    last_day = num[-1]
    buy_cnt = 0

    for i in range(len(num)-1, -1, -1):
        #print(i)
        if last_day > num[i]:
            buy_cnt += last_day - num[i]
        #print(buy_cnt)
        else:
            last_day = num[i]
        #print(buy_cnt)
    print(f'#{t} {buy_cnt}')