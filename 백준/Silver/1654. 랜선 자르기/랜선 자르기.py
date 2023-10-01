k, n = map(int, input().split())
l = sorted([int(input()) for _ in range(k)])

start, end = 1, l[-1]

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in l:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)