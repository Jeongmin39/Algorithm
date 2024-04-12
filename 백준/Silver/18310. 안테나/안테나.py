N = int(input())
houses = list(map(int, input().split()))

houses.sort()
mid_one = houses[N//2 - 1]
mid_two = houses[N//2]

sum_one, sum_two = 0, 0
for house in houses:
    sum_one += abs(house - mid_one)
    sum_two += abs(house - mid_two)
    
antenna = mid_one if sum_one <= sum_two else mid_two
print(antenna)