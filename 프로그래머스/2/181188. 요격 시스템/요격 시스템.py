def solution(targets):
    targets.sort(key = lambda x:x[1])
    
    count, end = 0, 0
    for s, e in targets:
        if s >= end:
            count += 1
            end = e        
    return count