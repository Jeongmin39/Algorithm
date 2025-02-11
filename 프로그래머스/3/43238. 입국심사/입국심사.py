def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        
        total = 0
        for time in times:
            total += mid // time
            if total >= n:
                break
                
        if total < n:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
            
    return answer