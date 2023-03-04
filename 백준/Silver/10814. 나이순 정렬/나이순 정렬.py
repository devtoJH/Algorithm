N = int(input())
case = []

for i in range(N):
    age, name = input().split()
    # print(age, name)
    case.append([int(age), i, name])
case.sort()
# print(case)

for j in range(len(case)):
    # print(j)
    print(f"{case[j][0]} {case[j][2]}")