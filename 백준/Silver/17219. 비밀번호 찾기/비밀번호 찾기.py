n, m = map(int, input().split())
li = {}

for i in range(n):
  address, password = input().split()
  li[address] = password

for j in range(m):
  print(li[input()])