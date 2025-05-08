def dfs(numbers, target, depth, total):
    global count
    
    if(depth == len(numbers)):
        if(target == total):
            count += 1
        return 
    
    plus = total + numbers[depth]
    minus = total - numbers[depth]
    
    dfs(numbers, target, depth+1, plus)
    dfs(numbers, target, depth+1, minus)
    
def solution(numbers, target):
    global count
    count = 0
    dfs(numbers, target, 0, 0)
    return count