def solution(num_list, n):
    answer = []

    check = 1
    for idx in range(0, len(num_list), n):
        temp = []
        for j in range(idx, n * check):
            temp.append(num_list[j])
        answer.append(temp)
        check += 1

    return answer