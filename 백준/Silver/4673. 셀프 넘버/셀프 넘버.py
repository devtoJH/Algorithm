n = set(range(1, 10001))
m = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    m.add(i)
n = n - m
for k in sorted(n):
    print(k)