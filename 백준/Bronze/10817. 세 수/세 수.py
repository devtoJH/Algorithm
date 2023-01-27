num = list(map(int, input().split()))
num.sort()

# 3개의 정수가 모두 다를 때
if num[0] < num[1] < num[2]: # 10 20 30
    print(num[1])

# 2개의 정수가 같고 하나만 다를 때
if num[0] == num[1] and num[0] < num[2]: # 10 10 20
    print(num[0])
elif num[1] == num[2] and num[0] < num[1]: # 10 20 20
    print(num[1])

# 3개의 정수 모두 같을 때
if num[0] == num[1] == num[2]: # 10 10 10
    print(num[0])