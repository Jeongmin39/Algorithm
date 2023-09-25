arr = [int(input()) for _ in range(9)]
remain = sum(arr) - 100
f1, f2 = 0, 0

for i in range(8):
    for j in range(i+1, 9):
        if (arr[i]+arr[j] == remain):
            f1 = arr[i]
            f2 = arr[j]

arr.remove(f1)
arr.remove(f2)
arr.sort()

for i in arr:
    print(i)