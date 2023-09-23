n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
s = []

def dfs(arr):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(arr, n):
        if n_list[i] not in s:
            s.append(n_list[i])
            dfs(i+1)
            s.pop()

dfs(0)