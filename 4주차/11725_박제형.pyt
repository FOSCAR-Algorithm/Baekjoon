# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

# Recursion Error
import sys
sys.setrecursionlimit(10**6) # 백준 프로그램에서는 recursion limit이 100으로 제한, 이 문제에서는 N <= 100,000 이므로 Recursino limit을 늘려줘야함

def dfs(node):
    visited[node] = 1
    for i in Tree[node]:
        if visited[i] == 0:
            ParentNode[i] = node
            dfs(i)

N = int(input())

Tree = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

# 숫자가 랜덤하게 들어가있음 -> 낮은 숫자부터 탐색하기 위해 sort
for i in range(N+1):
    Tree[i].sort()

# 각 노드의 parent 값을 저장하는 list (인덱스 : 자식노드, 값 : 부모노드)
ParentNode = [0] * (N+1)
# 각 노드의 방문 여부를 저장하는 list
visited = [0] * (N+1)

dfs(1)

print(*ParentNode[2:], sep='\n')