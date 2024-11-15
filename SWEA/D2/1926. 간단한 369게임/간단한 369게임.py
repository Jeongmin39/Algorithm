T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    i_str = str(i)
    count = i_str.count('3') + i_str.count('6') + i_str.count('9')
    if count > 0:
        print("-" * count, end = ' ')
    else:
        print(i, end = ' ')
