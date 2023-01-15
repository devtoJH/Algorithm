import sys
T = int(input())
for t in range(1, T+1):
    n, m = map(int, sys.stdin.readline().split())
    print(n + m)