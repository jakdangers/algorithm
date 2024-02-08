def solution(line):
    n = len(line)

    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')

    cross = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            a, b, e = line[i]
            c, d, f = line[j]

            if (a * d) - (b * c) == 0:
                continue

            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if x == int(x) and y == int(y):
                cross.append((int(x), int(y)))

                max_x = max(max_x, int(x))
                min_x = min(min_x, int(x))
                max_y = max(max_y, int(y))
                min_y = min(min_y, int(y))

    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 1
    print(max_y, min_y)

    map = [["."] * len_x for _ in range(len_y)]

    for x, y in cross:
        nx = 0
        ny = 0

        if min_x < 0:
            nx = x + abs(min_x)
        else:
            nx = x - min_x

        if min_y < 0:
            ny = y + abs(min_y)
        else:
            ny = y - min_y

        map[ny][nx] = "*"

    result = []

    for m in map:
        result.append("".join(m))

    return result[::-1]