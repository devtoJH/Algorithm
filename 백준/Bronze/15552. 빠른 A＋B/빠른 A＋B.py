import sys
T = int(sys.stdin.readline())
for t in range(1, T+1):
    n, m = map(int, sys.stdin.readline().split())
    print(n + m)