from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    for cloth in clothes:
        clothes_dict[cloth[1]] += 1
    
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)
        
    return answer - 1