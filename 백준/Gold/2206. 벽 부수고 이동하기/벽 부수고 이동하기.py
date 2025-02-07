import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    
    queue = deque([(x, y, 0, 0)])
    visited[x][y][0] = True

    while queue:
        x, y, broke, distance = queue.popleft()

        if (x, y) == (n-1, m-1):
            return distance + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and broke == 0:
                    if not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        queue.append((nx, ny, 1, distance + 1))

                elif graph[nx][ny] == 0 and not visited[nx][ny][broke]:
                    visited[nx][ny][broke] = True
                    queue.append((nx, ny, broke, distance + 1))

    return -1

print(bfs(0,0))