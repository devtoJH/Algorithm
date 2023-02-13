x, y = list(map(str, input().split()))
Rev_x = x[::-1]
Rev_y = y[::-1]

if Rev_x == '01' or Rev_x == '001' or Rev_x == '1000':
    Rev_x = 1
if Rev_y == '01' or Rev_y == '001' or Rev_y == '1000':
    Rev_y = 1

cnt = int(Rev_x) + int(Rev_y)

if cnt == 10 or cnt == 100 or cnt == 1000:
    cnt = 1

print(int(str(cnt)[::-1]))