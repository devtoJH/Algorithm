n, m = map(int, input().split())
n_list = list(map(int, input().split()))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in sorted(n_list):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()