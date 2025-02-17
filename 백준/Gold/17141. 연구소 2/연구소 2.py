import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(virus):
    queue = deque(virus)
    visited = [[-1] * n for _ in range(n)]
    m = 0
    for x, y in virus:
        visited[x][y] = 0

    while queue:
        i, j = queue.popleft()
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[i][j] + 1
                    queue.append((nx, ny))
                    m = max(visited[i][j] + 1, m)

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 1 and visited[i][j] == -1:
                return float('inf')
    return m  

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
viruses = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            viruses.append((i, j))

answer = float('inf')
for virus in combinations(viruses, m):
    answer = min(bfs(virus), answer)

if answer == float('inf'):
    print(-1)
else:
    print(answer)