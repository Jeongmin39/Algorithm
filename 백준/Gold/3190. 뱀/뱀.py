N = int(input())
board = [[0] * (N) for _ in range(N)] # 빈 공간 : 0

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 # 사과 위치 : 1

L = int(input())
times = [0] * 10000
for _ in range(L):
    when, dir = input().split()
    times[int(when)] = dir

snake = []
snake.append([0,0])
board[0][0] = 2 # 뱀 위치 : 2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]
dir = 1
nx, ny = 0, 0 
time = 0

while(True):
    time += 1
    nx += dx[dir]
    ny += dy[dir]

    if (nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2):
        break

    if (board[nx][ny] == 1): # 사과 있으면
        snake.append([nx, ny])
        board[nx][ny] = 2 

    elif (board[nx][ny] == 0): # 사과 없으면
        snake.append([nx, ny])
        board[nx][ny] = 2

        delX, delY = snake.pop(0)
        board[delX][delY] = 0

    if (times[time] == 'D'):
        dir = (dir + 1) % 4
    elif (times[time] == 'L'):
        dir = (dir + 3) % 4

print(time)