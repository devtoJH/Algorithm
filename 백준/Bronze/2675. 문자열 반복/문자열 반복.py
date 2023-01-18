T = int(input())
for t in range(1, T+1):
    R, S = input().split()
    for i in range(len(S)):
        a = S[i] * int(R)
        print(a, end='')
    print()