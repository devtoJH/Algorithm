from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
d = deque()

for n in range(N):
    c = list(map(int, input().split()))

    if c[0] == 1:
        d.insert(0, c[1])
    elif c[0] == 2:
        d.append(c[1])
    elif c[0] == 3:
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif c[0] == 4:
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif c[0] == 5:
        print(len(d))
    elif c[0] == 6:
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 7:
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif c[0] == 8:
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])