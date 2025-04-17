from itertools import permutations

def solution(k, dungeons):
    answer = -1
    temp_k = k
    
    data = list(permutations(dungeons, len(dungeons)))
    for i in data:
        count = 0
        for need, use in i:
            if temp_k >= need:
                temp_k -= use
                count += 1
                answer = max(answer, count)
            else:
                temp_k = k
                break
    return answer