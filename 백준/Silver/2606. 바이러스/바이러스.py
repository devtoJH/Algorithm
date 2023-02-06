n = int(input()) # 정점 개수(컴퓨터)
m = int(input()) # 간선 개수(바이러스)

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 1번 컴퓨터를 시작 정점으로 DFS 진행
def dfs(m):
    visited[m] = 1
    for adj in graph[m]:
        if visited[adj] == 0:
            dfs(adj)
dfs(1)
print(sum(visited) - 1)