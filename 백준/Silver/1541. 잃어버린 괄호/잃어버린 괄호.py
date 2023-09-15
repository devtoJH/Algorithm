a = input().split('-')

a_min = 0

for i in a[0].split('+'):
    a_min += int(i)

for i in a[1:]:
    for j in i.split('+'):
        a_min -= int(j)

print(a_min)