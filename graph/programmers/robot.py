from collections import deque


def solution(maps):
    n = len(maps) # row
    m = len(maps[0]) # col

    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue

                if (maps[nx][ny] == 1):
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

    bfs(0, 0)

    if maps[n - 1][m - 1] == 1:
        answer = -1
    else:
        answer = maps[n - 1][m - 1]

    return answer