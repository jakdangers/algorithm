def solution(quiz):
    answer = []

    for q in quiz:
        terms = q.split(" ")
        a = int(terms[0])
        op = terms[1]
        b = int(terms[2])
        result = int(terms[4])

        if op == "+" and a + b == result:
            answer.append("O")
        elif op == "-" and a - b == result:
            answer.append("O")
        else:
            answer.append("X")

    return answer