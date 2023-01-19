number = list(map(int, input().split()))
sum_list = []
for i in range(len(number)):
    a = number[i] ** 2
    sum_list.append(a)
print(sum(sum_list)%10)