x, y = map(int, input().split())

print(int(x + y + min(x, y) // 10))