from collections import defaultdict
def solution(genres, plays):
    g_dict = defaultdict(int)
    t_dict = defaultdict(list)

    n = len(genres)

    for i in range(n):
        g_dict[genres[i]] += plays[i]
        t_dict[genres[i]].append((i, plays[i]))

    rank = sorted(g_dict.items(), key=lambda x: x[1], reverse=True)

    result = []
    for g, _ in rank:
        target = sorted(t_dict[g], key=lambda x: (x[1], -x[0]), reverse=True)[:2]
        for i, _ in target:
            result.append(i)

    return result