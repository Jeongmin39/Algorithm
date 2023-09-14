num = int(input())
n_list = list(map(int, input().split()))

min = min(n_list)
max = max(n_list)
N = min*max
print(N)