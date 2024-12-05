A, P = map(int, input().split())
current_num = A
nums = [current_num]

while True:
    temp = str(current_num)
    num = 0
    
    for i in temp:
        num += int(i) ** P
    
    if num in nums:
        nums = nums[:nums.index(num)]
        break
    else:
        nums.append(num)
        current_num = num
        
print(len(nums))