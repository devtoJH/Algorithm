n = int(input())
num = []
for i in range(1, n+1):
    for m in range(1, n+1):
        if i * m == n:
            num.append(i)
num.sort()
print(*num)