import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [[] for _ in range (N+1)]
distance = [-1] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

def bfs(start):
    result = []
    queue = deque([start])
    distance[start] = 0

    while queue:
        now = queue.popleft()
        for next_city in graph[now]:
            if distance[next_city] == -1:
                distance[next_city] = distance[now] + 1
                queue.append(next_city)
                if distance[next_city] == K:
                    result.append(next_city)

    if result:
        result.sort()
        for i in result:
            print(i, end = '\n')
    else:
        print(-1)

bfs(X)