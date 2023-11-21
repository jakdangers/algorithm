def solution(emergency):
    answer = []

    sort_emergency = sorted(emergency, reverse=True)

    for num in emergency:
        for idx in range(len(emergency)):
            if num == sort_emergency[idx]:
                answer.append(idx + 1)

    return answer