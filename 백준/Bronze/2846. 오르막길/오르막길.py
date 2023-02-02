N = int(input())
height = list(map(int, input().split()))
a = 0
rise_road = []

for i in range(N-1):
    if height[i] < height[i+1]:
        a += height[i+1] - height[i]
    #print(a)
    else:
        rise_road.append(a)
        a = 0

rise_road.append(a)
print(max(rise_road))
