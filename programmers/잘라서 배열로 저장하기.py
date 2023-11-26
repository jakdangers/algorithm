def solution(my_str, n):
    answer = []

    for i in range(0, len(my_str), n):
        count = 0
        text = ""

        end = i + n
        if i + n > len(my_str):
            end = len(my_str)

        for j in range(i, end):
            text += my_str[j]

        answer.append(text)

    return answer