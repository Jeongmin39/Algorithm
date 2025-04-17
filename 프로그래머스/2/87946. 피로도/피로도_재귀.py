def solution(k, dungeons):
    n = len(dungeons)
    max_count = 0
    visited = [False] * n
    
    def dfs(current_k, count):
        nonlocal max_count
        max_count = max(max_count, count)
        
        for i in range(n):
            need, use = dungeons[i]
            if not visited[i] and current_k >= need:
                visited[i] = True
                dfs(current_k - use, count + 1)
                visited[i] = False
        
    dfs(k, 0)
    return max_count    
