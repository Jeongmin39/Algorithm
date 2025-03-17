import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
NGE = [-1] * N
stack = []

for i in range(N - 1, -1, -1):
    while stack:
        if stack[-1] > arr[i]:
            NGE[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(arr[i])

for i in NGE:
    print(i, end = ' ')