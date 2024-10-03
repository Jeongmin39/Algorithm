import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()

# 산술평균
print(round(sum(data)/n))

# 중앙값
print(data[n//2])

# 최빈값
count = dict()
for i in data:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

cnt_max = max(count.values())
max_lst = []
for i in count:
    if count[i] == cnt_max:
        max_lst.append(i)

print(max_lst[0]) if len(max_lst) == 1 else print(max_lst[1])

# 범위
print(data[n-1] - data[0])