def make_map(lock, M, Size):
    Map = [[2] * Size for _ in range(Size)]
    Point = 0 # 홈 부분의 개수
    lock_x, lock_y = 0, 0
    # 실제 자물쇠 부분
    for i in range(M - 1, Size - (M - 1)):
        for j in range(M - 1, Size - (M - 1)):
            Map[i][j] = lock[lock_x][lock_y]
            if Map[i][j] == 0:
                Point += 1
            lock_y += 1
        lock_y = 0
        lock_x += 1
    return Map, Point

def check_key_and_lock(Sx, Sy, key, Map, M):
    Check = 0
    x_Idx, y_Idx = 0, 0
    for x in range(Sx, Sx + M):
        for y in range(Sy, Sy + M):
            if Map[x][y] == 1 and key[x_Idx][y_Idx] == 1:
                return -1
            if Map[x][y] == 0 and key[x_Idx][y_Idx] == 0:
                return -1
            if Map[x][y] == 0 and key[x_Idx][y_Idx] == 1:
                Check += 1
            y_Idx += 1
        y_Idx = 0
        x_Idx += 1
    return Check
    
def rotate_key(key, M):
    temp = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            temp[i][j] = key[M - 1 - j][i]
    return temp

def move_map(key, lock, M, N):
    Size = N + 2 * (M - 1)
    Map, Point = make_map(lock, M, Size)
    for _ in range(4):
        for i in range(M + N - 1):
            for j in range(M + N - 1):
                Result = check_key_and_lock(i, j, key, Map, M)
                if Result == Point:
                    return True
        key = rotate_key(key, M)
    return False

def solution(key, lock):
    
    M = len(key)
    N = len(lock)
    
    return move_map(key, lock, M, N)