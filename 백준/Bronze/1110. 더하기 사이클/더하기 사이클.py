N = input()

if int(N) < 10:
    N = '0' + N

sum_N = N[1] + str(int(N[0]) + int(N[1]))[-1]
cycle = 1

while sum_N != N:
    sum_N = sum_N[1] + str(int(sum_N[0]) + int(sum_N[1]))[-1]
    cycle += 1
print(cycle)