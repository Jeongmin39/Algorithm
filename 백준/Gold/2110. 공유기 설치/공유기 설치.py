# distance로 공유기를 설치할 때 설치 가능한 공유기의 개수 계산
def install_count(houses, distance):
    count = 1
    last_locate = houses[0]

    for locate in houses[1:]:
        if locate - last_locate >= distance:
            count += 1
            last_locate = locate

    return count

# 가장 인접한 두 공유기 사이의 최대 거리 계산
def find_max_distance(houses, C):
    houses.sort()
    start, end = 1, houses[-1] - houses[0]

    while start <= end:
        mid = (start + end) // 2
        if install_count(houses, mid) < C:
            end = mid - 1
        else:
            start = mid + 1

    return start - 1

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
    
print(find_max_distance(houses, C))