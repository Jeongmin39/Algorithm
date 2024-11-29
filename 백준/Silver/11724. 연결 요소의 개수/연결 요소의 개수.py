import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
count = 0

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(graph, i, visited)
        
print(count)

"""
반복문 이용하여 처리

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for i in graph[v]:
                if not visited[i]:
                    stack.append(i)
                    
count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)
        
print(count)
"""
