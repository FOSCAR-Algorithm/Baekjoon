# DFS와 BFS
# https://www.acmicpc.net/problem/1260

from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

# 각 정점별로 연결된 Node True로 표시
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

def dfs(V):
    visited_dfs[V] = True
    print(V, end=' ')
    
    for i in range(N+1):
        if not visited_dfs[i] and graph[V][i]:
            dfs(i)

def bfs(V):
    queue = deque([V])
    visited_bfs[V] = True
    
    while queue:
        
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if not visited_bfs[i] and graph[V][i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(V)
print()
bfs(V)