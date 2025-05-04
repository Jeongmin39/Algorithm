from collections import Counter

def solution(nums):
    count = Counter(nums)
    count_list = list(count.keys())
    if len(count_list) >= len(nums) / 2:
        return len(nums) / 2
    else:
        return len(count_list)