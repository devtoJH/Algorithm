n = int(input())
name_dict = {}
for i in range(n):
    name, state = map(str, input().split())
    #print(name, state)
    if state == 'enter':
        name_dict[name] = 1
    else:
        del name_dict[name]
#print(sorted(name_dict.keys())[::-1])

for j in sorted(name_dict.keys())[::-1]:
    print(j)