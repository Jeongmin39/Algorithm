from itertools import combinations

# 치킨거리 계산
def calculate_distance(houses, chickens):
    city_distance = 0
    for hx, hy in houses:
        distance = float('inf')
        for cx, cy in chickens:
            distance = min(distance, (abs(hx - cx) + abs(hy - cy)))
        city_distance += distance
    return city_distance

N, M = map(int, input().split())
city = [] # 도시 정보
for _ in range(N):
    data = list(map(int, input().split()))
    city.append(data)

# 0 == 빈 칸 / 1 == 집 / 2 == 치킨집
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

min_distance = float('inf')
for M_chickens in combinations(chickens, M):
    min_distance = min(min_distance, calculate_distance(houses, M_chickens))

print(min_distance)