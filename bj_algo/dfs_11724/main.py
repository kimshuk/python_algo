import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited=[False]*(N+1)
count = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(curr):
    visited[curr] = True
    for i in graph[curr]:
        if not visited[i]:
            dfs(i)


for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1


print(count)