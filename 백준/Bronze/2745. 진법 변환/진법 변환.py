n, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = n[::-1]
result = 0

for i, j in enumerate(n):
    result += (int(b) ** i) * (ary.index(j))
print(result)