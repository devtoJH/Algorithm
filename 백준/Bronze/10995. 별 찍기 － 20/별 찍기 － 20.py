n = int(input())

for i in range(n):
  if i % 2 == 1:
    print(" ", end="")
  print("* " * (n-1) + "*")