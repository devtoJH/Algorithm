n = int(input())
n_list = []

for _ in range(n):
    n_list.append(list(map(int, input().split())))

n_list.sort(key=lambda x : (x[1], x[0]))
start = 0
result = 0

for schedule in n_list:
    if schedule[0] >= start:
        start = schedule[1]
        result += 1

print(result)