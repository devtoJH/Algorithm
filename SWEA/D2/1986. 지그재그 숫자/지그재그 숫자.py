T = int(input())


for t in range(1, T+1):
    cnt = 0
    n = int(input())
    
    for i in range(1, n+1):
        if i % 2 == 1:
            cnt += i
        else:
            cnt -= i
    print(f'#{t} {cnt}')