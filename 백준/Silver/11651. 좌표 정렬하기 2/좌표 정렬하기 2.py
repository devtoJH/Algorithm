N = int(input())

num = []

for n in range(N):
    x, y = map(int, input().split())
    num.append([y, x])

num_list = sorted(num)

for y, x in num_list:
    print(x, y)