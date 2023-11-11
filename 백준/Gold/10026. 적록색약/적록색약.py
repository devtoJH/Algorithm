import sys
#sys.stdin = open('백준/input.txt')
from collections import deque

def bfs(i, j, color, arr):
    queue = deque()
    queue.append((i, j))    # matrix[i][j]부터 bfs 시작
    arr[i][j] = 0   # 방문 처리

    while queue:
        x, y = queue.popleft()
        for idx in range(4):    # 상, 하, 좌, 우
            nx = x + dx[idx]
            ny = y + dy[idx]
            # 인덱스가 범위를 벗어나는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 같은 색일 경우 방문 처리하고 queue에 넣기
            if arr[nx][ny] == color:
                arr[nx][ny] = 0
                queue.append((nx, ny))


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline()) for _ in range(n)] # 적록색약 아닌
matrix_rg = [[0] * n for _ in range(n)]    # 적록색약

# 적록색약의 matrix(초록색을 모두 빨간색으로 바꿈)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R' or matrix[i][j] == 'G':
            matrix_rg[i][j] = 'R'
        else:
            matrix_rg[i][j] = 'B'

answer = 0
answer_rg = 0
for i in range(n):
    for j in range(n):
        # 적록색약 아닌 사람
        if matrix[i][j] != 0:
            bfs(i, j, matrix[i][j], matrix)
            answer += 1
        # 적록색약인 사람
        if matrix_rg[i][j] != 0:
            bfs(i, j, matrix_rg[i][j], matrix_rg)
            answer_rg += 1
            
print(answer, answer_rg)