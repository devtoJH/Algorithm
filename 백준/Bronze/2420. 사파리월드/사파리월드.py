N, M = list(map(int, input().split()))
n = N - M
if n < 0:
    print(n * -1)
else:
    print(n)