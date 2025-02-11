import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
result = 0

while left <= right:
    total = 0
    mid = (left + right) // 2

    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total < m:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)