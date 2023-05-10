from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited=[False]*(N+1)
visited2=[False]*(N+1)


print(f'before:{graph}')


for _ in range(M):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

print(f'completed:{graph}')
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]


def dfs(curr):
    print(curr, end=" ")
    visited[curr] = True
    for i in graph[curr]:
        if not visited[i]:
            dfs(i)


def bfs(curr):
    visited2[curr] = True
    Q=deque([curr])
    while Q:
        c=Q.popleft()
        print(c, end=" ")
        for i in graph[c]:
            if not visited2[i]:
                Q.append(i)
                visited2[i]=True


dfs(V)
print()
bfs(V)


