str = input()
zero_cnt = 0 #0이 연속된 부분
one_cnt = 0 #1이 연속된 부분

if (str[0] == '0'):
    zero_cnt += 1
else:
    one_cnt += 1

for i in range(1, len(str)):
    if (str[i] != str[i-1]):
        if (str[i] == '0'):
            zero_cnt += 1
        else:
            one_cnt += 1

print(min(zero_cnt, one_cnt))