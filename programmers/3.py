def solution(parking):
    # 부모 노드인 경우를 제외
    def is_parent(tree, parent, child):
        while child in tree:
            if tree[child] == parent:
                return True
            child = tree[child]
        return False

    tree = {}
    for i, (left, right) in enumerate(parking):
        if left != -1:
            tree[left] = i
        if right != -1:
            tree[right] = i

    # TODO : 노드 3개가 편향 그래프인지 체크
    count = 0
    for i in range(len(parking)):
        for j in range(i + 1, len(parking)):
            if not (is_parent(tree, i, j) or is_parent(tree, j, i)):
                count += 1

    return count



from collections import defaultdict
import copy

def solution(card, word):
    def valid_word(card_chars_copy, word):
        line = [False] * 3
        found = True

        for char in word:
            char_found = False
            for index in card_chars_copy:
                if card_chars_copy[index][char] > 0:
                    card_chars_copy[index][char] -= 1
                    line[index] = True
                    char_found = True
                    break
            if not char_found:
                found = False
                break

        return found and all(line)

    # 각 줄 마다 어떠한 알파벳을 포함하고 있는지 저장
    card_chars = {
        i: defaultdict(int) for i in range(len(card))
    }

    # 하나의 요소를 하나의 줄로 생각하고 1 : {'A': 2, 'B': 1{}
    for index, str_ele in enumerate(card):
        for char in str_ele:
            card_chars[index][char] += 1

    answer = []

    for target_word in word:
        copied = copy.deepcopy(card_chars)
        if valid_word(copied, target_word):
            answer.append(target_word)

    if not answer:
        return ["-1"]

    return answer