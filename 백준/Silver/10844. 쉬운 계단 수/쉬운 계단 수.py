n = int(input())
d = [[0] * 12 for _ in range(n+1)]
d[1][2:11] = [1] * 9

for i in range(2, n+1):
    for j in range(1, 11):
        d[i][j] = d[i-1][j-1] + d[i-1][j+1]

answer = sum(d[n])
print(answer % 1000000000)