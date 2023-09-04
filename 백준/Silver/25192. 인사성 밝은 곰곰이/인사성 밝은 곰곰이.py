import sys
input = sys.stdin.readline

n = int(input())
e_set = set()
cnt = 0

for i in range(n):
  enter = input().strip()
  if enter == "ENTER":
    cnt += len(e_set)
    e_set.clear()
  else:
    e_set.add(enter)
cnt += len(e_set)

print(cnt)