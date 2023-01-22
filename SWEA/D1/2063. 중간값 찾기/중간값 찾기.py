N = int(input())
num = list(map(int, input().split()))
num.sort()
a = num[N//2]
print(a)