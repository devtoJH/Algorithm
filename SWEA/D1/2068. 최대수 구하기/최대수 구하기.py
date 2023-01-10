T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
    a = list(map(int,input().split()))
    # print(*a)
    n = max(a)
    print(f"#{t} {n}")
    pass