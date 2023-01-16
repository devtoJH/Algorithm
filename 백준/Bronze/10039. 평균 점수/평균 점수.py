result = 0
for i in range(5):
    num = int(input())
    if num > 40:
        result += num
    else:
        result += 40
print(int(result / 5))