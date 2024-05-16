# 탈옥 - 포기

from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
h, w = map(int, input().split())

whole_map = []
criminal = []
# arr = [[0 for j in range(cols)] for i in range(rows)]
# 20 * 10 => ********** 밑으로 20개 있는거임 [19][9] 10 = w 너비 20 = h 높이


for i in range(h):
    whole_map.append([])
    a = input()
    for j in range(w):
        if (a[j] == '$'):
            criminal.append((i, j))
        whole_map[i].append(a[j])

# 어디가 시작점일까..
# whole[0][j] , whole[i][0]. whole [끝][j], whole[i][끝]
escape = []

for i in range(w):
    if (whole_map[0][i]) == "." or (whole_map[0][i]) == "#":
        escape.append((0, i))
    if (whole_map[h - 1][i]) == "." or (whole_map[h - 1][i]) == "#":
        escape.append((h - 1, i))

for i in range(h):
    if (whole_map[i][0]) == "." or (whole_map[i][0]) == "#":
        escape.append((i, 0))
    if (whole_map[i][w - 1]) == "." or (whole_map[i][w - 1]) == "#":
        escape.append((i, w - 1))


min_doors = 999  # 최소 문 개수
door = 0 # 문 연개수


def find_path(start, end, doors, maps):
    if start == end:
        return doors
    if start[0] >= h or start[1] >= w:
        return
    if start[0] < 0 or start[1] < 0:
        return
    sx, sy = start
    if maps[sx][sy] == "#":
        maps[sx][sy] = "."
        doors += 1
    if sx > end[0] and sy > end[1]:
        digonal2 = (sx - 1, sy - 1)
        find_path(digonal2, end, doors, maps)

    if sx > end[0] and sy < end[1]:
        digonal4 = (sx - 1, sy + 1)
        find_path(digonal4, end, doors, maps)

    if sx < end[0] and sy < end[1]:
        digonal = (sx + 1, sy + 1)
        find_path(digonal, end, doors, maps)

    if sx < end[0] and sy > end[1]:
        digonal3 = (sx+1, sy-1)
        find_path(digonal3,end,doors,maps)

    down = (sx+1, sy)
    right = (sx, sy+1)
    up = (sx-1, sy)
    left = (sx, sy-1)


    find_path(up, end, doors, maps)
    find_path(left, end, doors, maps)
    find_path(down, end, doors, maps)
    find_path(right, end, doors, maps)



def dfs(criminal, escapes, doors):
    global min_doors
    if len(criminal) == 0:
        return min_doors

    for es in escapes:
        doors = 0
        curr_maps = deepcopy(whole_map)
        cur_x, cur_y = criminal[0]
        curr = find_path(criminal[0], es, doors, curr_maps)
        del criminal[0]
        min_doors = min(curr, doors)

    return min_doors


print(dfs(criminal, escape, door))
