a, b = map(int, input().split())
num_list = []
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        num_list.append(i)

print(max(num_list))
print(max(num_list) * (a // max(num_list) * (b // max(num_list))))