T = int(input())
for t in range(1, T+1):
    string = input().split()
    for i in string:
        print(i[::-1], end=' ')