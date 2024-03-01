from collections import defaultdict


def are_friends(graph, person1, person2):
    # 친구 관계 그래프에서 person1과 person2가 서로 친구인지 확인
    return person2 in graph[person1]


def find_friend_recommendations(graph):
    recommendations = []
    # 모든 사람들에 대해 친구 추천을 확인
    for person1 in graph:
        for person2 in graph:
            if person1 != person2 and not are_friends(graph, person1, person2):
                # A와 B가 친구이고 B와 C가 친구인 경우 A와 C를 추천
                for friend in graph[person1]:
                    if are_friends(graph, friend, person2):
                        recommendations.append((person1, person2))
                        break
    return recommendations


def find_friends_of_friends(graph, person):
    friends = set(graph[person])
    friends_of_friends = set()
    for friend in friends:
        friends_of_friends.update(graph[friend])
    # 친구의 친구 중 자신과 이미 친구인 사람은 제외
    friends_of_friends -= friends
    friends_of_friends.discard(person)
    return list(friends_of_friends)


# def solution(friends, user_id):
#     friend_dic = defaultdict(list)
#     for f1, f2 in friends:
#         friend_dic[f1].append(f2)
#         friend_dic[f2].append(f1)
#     print(friend_dic[user_id])
#     print("frink", friend_dic['frank'])
#     print("demi", friend_dic['demi'])
#
#     print(find_friends_of_friends(friend_dic, user_id))
def solution(friends, user_id):
    friend_dic = defaultdict(list)
    for f1, f2 in friends:
        friend_dic[f1].append(f2)
        friend_dic[f2].append(f1)

    friend_frequency = defaultdict(int)
    max_frequency = 0
    for friend in friend_dic[user_id]:
        for ff in friend_dic[friend]:
            if ff != user_id:
                friend_frequency[ff] += 1
                max_frequency = max(max_frequency, friend_frequency[ff])

    result = []
    for friend_name, frequency in friend_frequency.items():
        if frequency == max_frequency:
            result.append(friend_name)
    result.sort()

    return result


if __name__ == '__main__':
    print(solution([["david", "demi"], ["frank", "demi"], ["demi", "james"]], "frank"))
    print(solution([["david", "frank"], ["demi", "david"], ["frank", "james"], ["demi", "james"], ["claire", "frank"]],
                   "david"))

    # [["david", "demi"], ["frank", "demi"], ["demi", "james"]], "frank"

# def solution(friends, user_id):
#     friend_dic = defaultdict(list)
#     for f1, f2 in friends:
#         friend_dic[f1].append(f2)
#         friend_dic[f2].append(f1)
