n = int(input())
d = [50001] * (n+1)

if n >= 3:
    d[3] = 1
if n >= 5:
    d[5] = 1
    
for i in range(6, n+1):
    if d[i-3] != 50001 or d[i-5] != 50001:
        d[i] = min(d[i-3] + 1, d[i-5] + 1)

if d[n] == 50001:
    print(-1)
else:
    print(d[n])
    
"""
반복문 사용

n = int(input())
result = 0

while n >= 0:
    if n % 5 == 0:
        result += (n // 5)
        print(result)
        break
    n -= 3
    result += 1
else:
    print(-1)
"""