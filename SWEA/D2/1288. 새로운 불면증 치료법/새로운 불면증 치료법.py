T = int(input())

for t in range(1, T+1):
    n = int(input())
    s = set()
    cnt = 1
    
    while True:
        for i in list(str(n)):
            s.add(i)
        
        if len(s) == 10:
            break

        n //= cnt
        cnt += 1
        n *= cnt
        
    print(f'#{t} {n}')