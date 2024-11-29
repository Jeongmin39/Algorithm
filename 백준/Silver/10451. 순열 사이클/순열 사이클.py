import sys
    
def dfs(v):
    visited[v] = True
    nv = graph[v]
    if not visited[nv]:
        dfs(nv)
        
T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (n+1)
    cycle = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cycle += 1
    print(cycle)