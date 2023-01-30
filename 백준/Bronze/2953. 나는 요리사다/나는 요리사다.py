n_list = []

for i in range(5):
    n = list(map(int, input().split()))
    n_list.append(sum(n))
    
print(n_list.index(max(n_list))+1, max(n_list))