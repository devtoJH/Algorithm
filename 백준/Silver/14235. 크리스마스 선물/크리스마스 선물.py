import heapq

n = int(input())
heap = []
gift = []

for _ in range(n):

    a = input()
    if len(a) == 1:
        if heap: 
            print(heapq.heappop(heap)[1])
        else: 
            print(-1)
    else:
        gift = list(map(int, a.split()))
        for i in range(1, len(gift)): 
            heapq.heappush(heap, (-gift[i], gift[i]))