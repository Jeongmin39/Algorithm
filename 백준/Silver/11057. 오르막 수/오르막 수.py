n = int(input())
d = [[0] * 10 for _ in range(n+1)]
d[1][0:10] = [1] * 10

for i in range(2, n+1):
    for j in range(10):
        d[i][j] = sum(d[i-1][j:])
    
answer = sum(d[n])
print(answer % 10007)