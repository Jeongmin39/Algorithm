from operator import itemgetter

def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1))
    foods.sort()
    
    previous_time = 0
    for i, food in enumerate(foods):
        diff = food[0] - previous_time
        if diff != 0:
            spend_time = diff * n
            if spend_time <= k:
                k -= spend_time
                previous_time = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key = itemgetter(1))
                return sublist[k][1]
        n -= 1
        
    return -1 