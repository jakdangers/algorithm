def solution(A, B):
    if A == B:
        return 0

    length = len(A)
    temp = [""] * length
    for j in range(1, length):
        for i in range(length):
            temp[(i + j) % length] = A[i]
        if ''.join(temp) == B:
            return j

    return -1