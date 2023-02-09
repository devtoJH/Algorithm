n, k = map(int, input().split())

cnt = 1
for i in range(k):
    cnt *= n
    n -= 1

cnt1 = 1
for i in range(2, k+1):
    cnt1 *= i

print(cnt // cnt1)