# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    binary_N = ''
    while N != 0:
        if N % 2 == 1:
            binary_N += '1'
        else:
            binary_N += '0'
        N = N // 2

    binary_N = binary_N[::-1]
    max_gap = 0
    count = 0

    if binary_N.count('1') == 1:
        return 0


    for i in range(len(binary_N)):
        if binary_N[i] == '1':
            j = i + 1
            count = 0
            while j < len(binary_N):
                if binary_N[j] == '1':
                    i = j
                    break
                if j == len(binary_N)-1 and binary_N[j] == '0':
                    count = 0
                    break
                count += 1
                j += 1
        max_gap = max(max_gap, count)

    return max_gap


n = int(input())

print(solution(n))