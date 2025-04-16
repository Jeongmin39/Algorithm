import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
called = [[False] * 5 for _ in range(5)]

def check_row(): # 가로 빙고 확인
    cnt = 0
    for col in called:
        if sum(col) == 5:
            cnt += 1
    return cnt

def check_col(): # 세로 빙고 확인
    cnt = 0
    temp = list(map(list, zip(*called)))
    for col in temp:
        if sum(col) == 5:
            cnt += 1
    return cnt

def check_cross(): # 대각선 빙고 확인
    cnt = 0
    temp = 0
    for i in range(5):
        temp += called[i][i]
    if temp == 5:
        cnt += 1
    temp = 0
    for i in range(5):
        temp += called[i][5-i-1]
    if temp == 5:
        cnt += 1
    return cnt

def bingo(check):
    for col in range(5):
        for row in range(5):
            if check == board[col][row]:
                called[col][row] = True
                total = check_row() + check_col() + check_cross()
                return total >= 3
    return False

count = 0
found = False
for col in range(5):
    for row in range(5):
        count += 1
        check = call[col][row]
        if bingo(check):
            found = True
            break
    if found:
        break
print(count)