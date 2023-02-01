T = int(input())

for t in range(T):
    N = list(map(int, input().split()))
    N.remove(max(N))
    N.remove(min(N))
    #print(N)
    if max(N) - min(N) >= 4:
        print('KIN')
    else:
        print(sum(N))