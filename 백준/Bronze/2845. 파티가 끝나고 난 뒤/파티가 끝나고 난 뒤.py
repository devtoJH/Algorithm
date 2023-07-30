L, P = map(int, input().split())
person = list(map(int, input().split()))
for i in person:
    print(i - L * P, end = ' ')