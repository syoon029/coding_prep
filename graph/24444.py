import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n + 1)]

visited = [0] * (n+1)



cnt = 1


for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()




def bfs(graph, s, visited):
    global cnt
    vq = deque([s])
    visited[s] = cnt
    while vq:
        new = vq.popleft()
        for k in graph[new]:
            if visited[k] == 0:
                cnt += 1
                visited[k] = cnt
                vq.append(k)


bfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])
