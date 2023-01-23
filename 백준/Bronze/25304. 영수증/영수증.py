X = int(input())
N = int(input())

value = []

for i in range(N):
    a, b = map(int, input().split())
    value.append(a*b)

if sum(value) == X:
    print('Yes')
else:
    print('No')