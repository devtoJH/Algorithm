n, m = list(map(int, input().split()))
s = []

def dfs(arr):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(arr, n+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)