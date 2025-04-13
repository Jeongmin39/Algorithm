import heapq

def solution(jobs):
    
    jobs = sorted([(start, length, i) for i, (start, length) in enumerate(jobs)], key = lambda x: x[0])
    n = len(jobs)

    i = 0 # jobs에서 처리할 인덱스
    now_time = 0
    total_time = 0
    heap = []
    
    while i < n or heap:
        while i < n and jobs[i][0] <= now_time:
            start, length, num = jobs[i]
            heapq.heappush(heap, (length, start, num)) 
            i += 1
        
        if heap:
            length, start, num = heapq.heappop(heap)
            now_time += length
            total_time += now_time - start
        else:
            now_time = jobs[i][0]
        
    return total_time // n