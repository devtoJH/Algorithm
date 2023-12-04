def dfs():
    if len(r) == (n // 2):
        start.append(r[:])
        link.append(list(set(num) - set(r[:])))
    for i in range(1, n+1):
        if i > r[-1]:
            r.append(i)
            dfs()
            r.pop()

m = []
n = int(input())
for i in range(n):
    m.append(list(map(int, input().split())))
num = [i for i in range(1, n+1)]

# 모든 경우에 팀 안에 1번이 들어있으므로 1번이 들어간 모든 경우의 수를 출력
r = [1]
start = []
link = []
dfs()

# result = 스타트팀과 링크팀 점수차를 저장하는 리스트
result = []

for i in range(len(start)):
    start_sum = 0
    link_sum = 0
    for j in range(n//2):
        for _ in range(n//2):
            start_sum += m[start[i][j] - 1][start[i][_] - 1] 
            link_sum += m[link[i][j] - 1][link[i][_] - 1]
    result.append(abs(start_sum - link_sum)) 
print(min(result))