import sys
import bisect
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
lis = [array[0]]

for num in array:
    if lis[-1] < num:
        lis.append(num)
    else:
        idx = bisect.bisect_left(lis, num)
        lis[idx] = num
        
print(len(lis))