n, k = map(int, input().split())
vertical = [0] * 1000001

for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end):
        vertical[i] += 1

left, right, total = 0, 0, 0
flag = False

while left <= right < 1000001:
    if total == k:
        flag = True
        break
    elif total < k:
        total += vertical[right]
        right += 1
    else:
        total -= vertical[left]
        left += 1

if flag:
    print(left, right)
else:
    print("0 0")