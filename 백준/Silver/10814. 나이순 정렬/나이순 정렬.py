import sys
input = sys.stdin.readline

N = int(input())
case = []

for i in range(N):
    age, name = input().split()
    case.append([int(age), i, name])

case_li = sorted(case)
# print(case_li)

for j in range(len(case_li)):
    print(f"{case_li[j][0]} {case_li[j][2]}")