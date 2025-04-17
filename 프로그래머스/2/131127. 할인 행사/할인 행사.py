def solution(want, number, discount):
    answer = 0
    wishlist = {}
    
    for i in range(len(want)):
        wishlist[want[i]] = number[i]
        
    for i in range(len(discount) - 9):
        temp_wishlist = wishlist.copy() # 딕셔너리 복사
        for j in range(i, i+ 10):
            if discount[j] in temp_wishlist and temp_wishlist[discount[j]] != 0:
                temp_wishlist[discount[j]] -= 1
            else:
                break
        
        if sum(temp_wishlist.values()) == 0:
            answer += 1
            
    return answer