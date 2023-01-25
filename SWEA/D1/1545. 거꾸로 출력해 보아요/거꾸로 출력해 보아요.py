n = int(input())
a = []
for i in range(n+1):
    a.append(i)
print(*a[::-1])