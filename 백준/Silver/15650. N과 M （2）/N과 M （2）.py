n, m = list(map(int, input().split()))
s = []
def dfs(arr):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(arr, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)