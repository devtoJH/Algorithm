n = int(input())
n2 = set(map(int, input().split()))

m = int(input())
m2 = list(map(int, input().split()))

for _ in m2:
    if _ in n2:
        print("1")
    else:
        print("0")