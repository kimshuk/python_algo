M,N = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

