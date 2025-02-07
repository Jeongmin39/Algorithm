import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, history, count):
    max_count = count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in history:
            history.add(board[nx][ny])
            max_count = max(max_count, dfs(nx, ny, history, count + 1))
            history.remove(board[nx][ny])
            
    return max_count
    
print(dfs(0, 0, {board[0][0]}, 1))