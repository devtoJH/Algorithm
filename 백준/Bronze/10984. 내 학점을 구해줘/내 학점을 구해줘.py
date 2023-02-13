T = int(input())

for t in range(T):
    n = int(input())

    c_cnt = 0
    g_cnt = 0

    for _ in range(n):
        c, g = map(float, input().split())
        c = int(c)

        c_cnt += c
        g_cnt += float(c) * g

    g_cnt = round(g_cnt / c_cnt, 1)
    print(c_cnt, g_cnt)