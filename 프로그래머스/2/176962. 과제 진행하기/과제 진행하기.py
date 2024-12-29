def solution(plans):
    answer = []
    stack = []
    
    # 시간을 정수로 변환
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])

    # 시작 시간 순으로 정렬
    plans.sort(key = lambda x:x[1])

    for i in range(len(plans) - 1):
        stack.append(plans[i])
        diff = plans[i+1][1] - plans[i][1]
        
        while stack and diff:
            # 현재 과제를 끝낼 수 있는 경우
            if stack[-1][2] <= diff:
                diff -= stack[-1][2]
                answer.append(stack[-1][0])
                stack.pop()
            # 끝낼 수 없는 경우
            else:
                stack[-1][2] -= diff # 남은 시간 갱신
                diff = 0
    
    # 마지막 과제 처리
    answer.append(plans[-1][0])
    
    while stack:
        answer.append(stack[-1][0])
        stack.pop()
                
    return answer