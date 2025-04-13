import heapq

def solution(jobs):
    answer = 0
    q = []
    
    for i in range(len(jobs)):
        q.append((jobs[i][1], jobs[i][0], i))
        
    print(q)
    return answer