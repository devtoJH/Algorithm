import sys
input = sys.stdin.readline

N = int(input())
d = []

for n in range(N):
    c = input().split()

    if c[0] == 'push_front':
        d.insert(0, c[1])
    elif c[0] == 'push_back':
        d.append(c[1])
    elif c[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop(0))
    elif c[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop(-1))
    elif c[0] == 'size':
        print(len(d))
    elif c[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif c[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])