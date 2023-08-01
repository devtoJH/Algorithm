s = int(input())
cnt = 0
while s >= 0:
    if s%5==0:
        cnt += (s//5)
        print(cnt)
        break
    s -= 3
    cnt += 1
else:
    print(-1) 