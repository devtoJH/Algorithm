import sys, heapq

heap = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num:
		heapq.heappush(heap, (abs(num), num))
	else:
		if heap:
			print(heapq.heappop(heap)[1])
		else:
			print(0)