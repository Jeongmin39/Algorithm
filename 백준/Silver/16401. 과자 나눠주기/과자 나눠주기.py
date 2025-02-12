import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

left = 1
right = max(snacks)

result = 0
while left <= right:
    total = 0
    mid = (left + right) // 2

    for snack in snacks:
        if snack >= mid:
            total += snack // mid
            if total >= m:
                break
    
    if total < m:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)