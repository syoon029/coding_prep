import copy


def solution(A, K):
    # Implement your solution here

    if len(A) == 0:
        return []

    rotate = [0 for i in range(len(A))]

    for i in range(K):
        for j in range(0, len(A) - 1):
            rotate[j + 1] = A[j]

        rotate[0] = A[-1]
        A = copy.deepcopy(rotate)

    return A