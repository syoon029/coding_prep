def solution(n, computers):
    #BFS
    answer = 0
    visited = []
    queue = []
    for i in range(n):
        if i not in visited:
            queue.append(i)  #
            answer += 1

            while (queue):
                cur = queue.pop(0)
                for j in range(n):
                    if (computers[cur][j] == 1 and j not in visited):
                        queue.append(j)
                        visited.append(j)
    return answer

    #DFS
def solution(n, computers):
    answer = 0
    visited = []

    def newRoot (i,n,visited):
        for j in range(n): # for all adjancy
            if computers[i][j] == 1 and j not in visited:
                visited.append(j)
                newRoot(j,n,visited)

    for i in range(n):
        if i not in visited :
            visited.append(i)
            answer = answer+1
            newRoot(i,n,visited)

    return answer