from collections import deque

n, k = map(int, input().split())

deq = deque([i for i in range(1, n + 1)])

result = []

for _ in range(n):
    deq.rotate(-k)
    result.append(deq.pop())

print("<" + str(result)[1:-1] + ">")