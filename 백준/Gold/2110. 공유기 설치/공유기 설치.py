import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

start = 0
end = houses[-1] - houses[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    house = houses[0]
    count = 1

    for i in range(1, n):
        if houses[i] >= house + mid:
            house = houses[i]
            count += 1

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)