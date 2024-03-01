from collections import defaultdict

def solution(friends, user_id):
    # 친구의 관계를 만든다 (중복되는 경우 없으므로 중복 검사 X)
    friend_dic = defaultdict(list)
    for f1, f2 in friends:
        friend_dic[f1].append(f2)
        friend_dic[f2].append(f1)

    # 친구의 친구 중 가장 많이 나오는 친구를 선택하기 위해 출현빈도 카운트
    friend_frequency = defaultdict(int)
    max_frequency = 0
    for friend in friend_dic[user_id]:
        for ff in friend_dic[friend]:
            if ff != user_id:
                friend_frequency[ff] += 1
                max_frequency = max(max_frequency, friend_frequency[ff])

    result = []
    # 가장 높은 출현빈도를 갖은 친구의 친구를 선택 (동일 빈도인 경우 사전준 정렬)
    for friend_name, frequency in friend_frequency.items():
        if frequency == max_frequency:
            result.append(friend_name)
    result.sort()

    return result