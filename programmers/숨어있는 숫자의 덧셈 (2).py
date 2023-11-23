def solution(my_string):
    answer = 0

    numstr = ""
    for char in my_string:
        if char.isdigit():
            numstr += char
        else:
            if numstr != "":
                answer += int(numstr)
                numstr = ""

    if numstr != "":
        answer += int(numstr)

    return answer