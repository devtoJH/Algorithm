import sys
input = sys.stdin.readline

N = int(input())
q = []

for n in range(N):
    c = input().split()

    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif c[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])