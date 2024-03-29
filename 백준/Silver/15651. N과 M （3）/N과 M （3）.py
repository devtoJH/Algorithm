def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    
    for i in range(1, N+1):
        v[i] = 1
        dfs(n+1, lst+[i])
        v[i] = 0

N, M = map(int, input().split())
ans = []
v = [0] * (N+1)

dfs(0, [])
for lst in ans:
    print(*lst)