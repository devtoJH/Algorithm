num = list(map(int, input().split()))
while True:
    for i in range(len(num)-1):
        #print(i, end=' ')
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
            print(" ".join(map(str, num)))
    if num == [1, 2, 3, 4, 5]:
        break