T = int(input())

for t in range(1, T+1) :
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()

    print("#{}".format(t), end=' ')
    for i in range(N) :
        print(num[i], end=' ')
    print()