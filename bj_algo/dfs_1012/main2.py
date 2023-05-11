# BFS식 풀이법
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

T=int(input())
for _ in range(T):
    M,N,K=map(int, input().split())
    graph = [[0] * (M) for _ in range(N)]
    count = 0

    for _ in range(K):
        a,b=map(int, input().split())
        graph[b][a] = 1

    for i in range(N):
        for j in range(M):
            # 현재 위치에서 DFS 수행
            if graph[i][j] > 0:
                bfs(i, j)
                count += 1

    print(count)


