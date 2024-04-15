def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True)
    
    # 00 같은 경우를 처리하기 위해 str -> int -> str
    return str(int("".join(numbers)))