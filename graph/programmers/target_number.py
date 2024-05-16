def solution(numbers, targets):
    global answer
    answer = 0

    def dfs(i, total):
        global answer
        if i == len(numbers):
            if total == targets:
                answer += 1
            return

        dfs(i + 1, total + numbers[i])
        dfs(i + 1, total - numbers[i])
        return

    dfs(0,0)

    return answer
