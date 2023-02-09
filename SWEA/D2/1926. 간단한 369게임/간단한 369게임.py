n = int(input())

clap = ['3', '6', '9']
n_list = []

for i in range(1, n+1):
    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')
    
    if clap == 0:
        n_list.append(i)
    else:
        n_list.append('-' * clap)
print(*n_list)