import sys
input = sys.stdin.readline

N = int(input())
stick_list = []
cnt = 1

stick_list = [int(input()) for _ in range(N)]

max_stick = stick_list[-1]

for i in range(N-1, -1, -1):
    if stick_list[i] > max_stick:
        cnt += 1
        max_stick = stick_list[i]

print(cnt)