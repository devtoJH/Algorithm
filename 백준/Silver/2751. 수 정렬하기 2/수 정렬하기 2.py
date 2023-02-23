import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for _ in range(n):
    num = int(input())
    n_list.append(num)

for i in sorted(n_list):
    print(i)