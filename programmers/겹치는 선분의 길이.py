def solution(lines):
    points = []  # 선분의 시작과 끝 지점을 저장할 리스트

    for line in lines:
        start, end = line
        points.append((start, 1))  # 선분의 시작을 1로 표시
        points.append((end, -1))   # 선분의 끝을 -1로 표시

    points.sort()  # 지점을 정렬

    print(points)
    count = 0  # 겹치는 선분의 개수
    prev_point = None
    length = 0

    for point, delta in points:
        print(point, delta)
        if prev_point is not None:
            if count >= 2:
                length += point - prev_point  # 겹치지 않은 길이를 더함
        count += delta
        prev_point = point

    return length