A, P = map(int, input().split())
current_num = A
nums = [current_num]

while True:
    temp = str(current_num)
    num = 0
    
    for i in temp:
        num += int(i) ** P
    
    if num in nums:
        nums = nums[:nums.index(num)]
        break
    else:
        nums.append(num)
        current_num = num
        
print(len(nums))

"""
dfs 사용

A, P = map(int, input().split())
visited = [0] * 236197 # 최댓값 9 ** 5 + 9 ** 5 + 9 ** 5 + 9 ** 5
count = 1

def cal(A, P):
    result = 0
    for i in str(A):
        result += int(i) ** P
    return result

def dfs(A, P, count, visited):
    
    if visited[A] != 0:
        return visited[A] - 1
    
    visited[A] = count
    count += 1
    result = cal(A, P)
    return dfs(result, P, count, visited)

print(dfs(A, P, count, visited))
"""
