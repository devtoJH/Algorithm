num = [i for i in range(1, 31)]
for number in range(28):
    n = int(input())
    num.remove(n)
print(min(num))
print(max(num))