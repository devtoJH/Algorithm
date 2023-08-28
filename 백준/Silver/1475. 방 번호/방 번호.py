n = input()
n_list = [0] * 10
for i in range(len(n)):
    num = int(n[i])
    if num == 6 or num == 9:
        if n_list[6] <= n_list[9]:
            n_list[6] += 1
        else:
            n_list[9] += 1
    else:
        n_list[num] += 1
 
print(max(n_list))