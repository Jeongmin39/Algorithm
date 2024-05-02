from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] # 정점 1 ~ N
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
  graph[i].sort()

# DFS
def dfs(v):
    visited_dfs[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

# BFS
def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for i in graph[node]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(V)
print()
bfs(V)