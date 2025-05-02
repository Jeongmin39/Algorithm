from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    if visited[n-1][m-1] == 0:
        return -1
    else:
        return visited[n-1][m-1]                    