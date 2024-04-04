N = input()
half_length = len(N) // 2

left_sum = sum(map(int, N[:half_length]))
right_sum = sum(map(int, N[half_length:]))

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")