n =  int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_sort = sorted(a, reverse=True)
b_sort = sorted(b)

s = 0

for i in range(n):
  s += a_sort[i] * b_sort[i]
print(s)