import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

cnt = 0


def dfs(graph, r, visited):
    global cnt
    visited[r] = 1
    for i in graph[r]:
        if visited[i] == 0: # not visited
            cnt += 1
            visited[i] = 1
            dfs(graph, i, visited)


dfs(graph, 1, visited)

print(cnt)



