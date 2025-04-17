from collections import Counter

def solution(want, number, discount):
    answer = 0
    wishlist = dict(zip(want, number))
    window_size = 10
    
    window_counter = Counter(discount[:window_size])
    if window_counter == wishlist:
        answer += 1
        
    for i in range(1, len(discount) - window_size + 1):
        prev_item = discount[i - 1]
        next_item = discount[i + window_size - 1]
        
        window_counter[prev_item] -= 1
        if window_counter[prev_item] == 0:
            del window_counter[prev_item]
        
        window_counter[next_item] += 1
        
        if window_counter == wishlist:
            answer += 1
        
    return answer
