T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
    a = list(map(int,input().split()))
    n = sum(a)
    m = n / len(a)
    print(f"#{t} {round(m)}")
    pass