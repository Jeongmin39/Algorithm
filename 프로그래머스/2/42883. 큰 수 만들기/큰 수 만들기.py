def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while k > 0 and stack and num > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(num)
    answer = ''.join(stack[:len(stack)-k])
    return answer