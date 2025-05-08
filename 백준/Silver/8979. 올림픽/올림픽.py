n, k = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]
nations.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
same = 1
for i in range(n):

    if nations[i][0] == k:
        print(rank)
        break
    
    if i < n-1:
        if nations[i][1:] == nations[i+1][1:]:
            same += 1
        else:
            rank += same
            same = 1