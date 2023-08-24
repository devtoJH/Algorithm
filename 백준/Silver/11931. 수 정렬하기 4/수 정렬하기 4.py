import sys
input = sys.stdin.readline

N = int(input())

num = []

for _ in range(0, N):
    num.append(int(input()))

num.sort()
num.reverse()
for i in range(0, N):
    print(num[i])