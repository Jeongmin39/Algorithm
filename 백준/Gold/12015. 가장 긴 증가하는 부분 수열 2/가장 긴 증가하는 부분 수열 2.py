import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
lis = [array[0]]

def find_place(target):
    start = 0
    end = len(lis) - 1
    
    while start <= end:
        mid = (start + end) // 2

        if lis[mid] == target:
            return mid
        elif lis[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start

for num in array:
    if lis[-1] < num:
        lis.append(num)
    else:
        idx = find_place(num)
        lis[idx] = num
        
print(len(lis))