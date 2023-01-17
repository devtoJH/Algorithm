x, y = [], []
for i in range(3):
    x_point, y_point = map(int, input().split())
    x.append(x_point)
    y.append(y_point)

for n in x:
    if x.count(n) == 1:
        print(n, end=' ')
        break

for m in y:
    if y.count(m) == 1:
        print(m, end=' ')
        break