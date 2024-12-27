# DFS
def dfs(n, com, computers, visited):
    visited[com] = True
    for i in range(n):
        if i != com and computers[com][i] == 1:
            if not visited[i]:
                dfs(n, i, computers, visited)
    
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for com in range(n):
        if not visited[com]:
            dfs(n, com, computers, visited)
            answer += 1
    return answer

"""
BFS

from collections import deque

def bfs(n, com, computers, visited):
    queue = deque([com])
    visited[com] = True
    while queue:
        com = queue.popleft()
        visited[com] = True
        for i in range(n):
            if i != com and computers[com][i] ==1 :
                if not visited[i]:
                    queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for com in range(n):
        if not visited[com]:
            bfs(n, com, computers, visited)
            answer += 1
    return answer
    
"""
