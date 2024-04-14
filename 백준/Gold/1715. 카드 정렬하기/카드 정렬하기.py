import heapq

N = int(input())
cards = []
count = 0

for _ in range(N):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    count += tmp
    heapq.heappush(cards, tmp)

print(count)