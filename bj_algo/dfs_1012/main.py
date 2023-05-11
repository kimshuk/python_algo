# DFS식 풀이법
import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
       nx = x + dx[i]
       ny = y + dy[i]

       if (0 <= nx < N) and (0 <= ny < M):
           if graph[nx][ny] == 1:
               graph[nx][ny] = -1
               dfs(nx, ny)

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
                dfs(i, j)
                count += 1

    print(count)


