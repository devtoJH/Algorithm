N, M = map(int, input().split())
A, B = [], []
for n in range(N):
    n = list(map(int, input().split()))
    A.append(n)
for n in range(N):
    n = list(map(int, input().split()))
    B.append(n)
for n in range(N):
    for m in range(M):
        print(A[n][m] + B[n][m], end=' ')
    print()