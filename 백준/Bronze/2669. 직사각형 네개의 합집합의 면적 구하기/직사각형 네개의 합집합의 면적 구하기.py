point = [[0]*101 for _ in range(101)]
n_list = []

for _ in range(4):
    l_x, l_y, r_x, r_y = map(int, input().split())
    for i in range(l_x, r_x):
        #print(i)
        for j in range(l_y, r_y):
            #print(j)
            point[i][j] = 1
        
print(sum(sum(point, [])))