num_list = []

for i in range(10):
    n = int(input())
    num_list.append(n % 42)

a = set(num_list)
print(len(a))