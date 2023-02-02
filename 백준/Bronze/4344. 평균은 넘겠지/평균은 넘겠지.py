C = int(input())

for c in range(C):
    average = []
    N = list(map(int, input().split()))
    N.pop(0)
    #print(N)
    #print(sum(N)/len(N))

    for i in range(len(N)):
        if sum(N)//len(N) < N[i]:
            average.append(N[i])
    #         print(N[i], end=' ')
    # print()
    a = (len(average)/len(N)) * 100
    print(f'{a:.3f}%')