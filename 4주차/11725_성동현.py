import sys
from collections import deque

def search_parent():


    N=int(input())
    graph=[[] for _ in range(N+1)]
    visited = ['True'] * (N + 1)
    parent_Node=[0]*(N+1)

    for i in range(N-1):
        a,b=map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # for i in range(len(graph)):
    #     graph[i].sort()

    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = 'False'
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if visited[i] == 'True':
                    parent_Node[i]=v #부모노드를 저장하는 코드
                    queue.append(i)
                    visited[i] = 'False'

    bfs(graph,1,visited)
    for i in range(2,len(parent_Node)):
        print(parent_Node[i])


if __name__=="__main__":
    search_parent()