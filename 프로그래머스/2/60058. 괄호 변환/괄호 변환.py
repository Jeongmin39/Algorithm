from collections import deque

# 두 문자열 u, v로 분리
def separate_str(p):
    l_paren, r_paren = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            l_paren += 1
        else:
            r_paren += 1
        if l_paren == r_paren:
            return p[:i+1], p[i+1:]

# 올바른 괄호 문자열 확인
def check_correct(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True if not stack else False
    
def solution(p):
    if p == '':
        return ''
    
    answer = ''
    u, v = separate_str(p)
    
    if check_correct(u) == True:
        answer = u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        
        for s in u[1:len(u)-1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('
    return answer