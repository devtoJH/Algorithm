n = int(input())
a = list(map(int, input().split()))

A = sorted(a)
b_list = []

for i in range(n):
    idx = A.index(a[i])
    b_list.append(idx)
    A[idx] = -1
print(*b_list)