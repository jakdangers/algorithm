from collections import defaultdict
import copy

def solution(card, target):
    # 각 줄 마다 어떠한 알파벳을 포함하고 있는지 저장
    card_chars = {
        i: defaultdict(int) for i in range(len(card))
    }

    # 각 카드 인덱스에 사용된 알파벳 파악
    for index, value in enumerate(card):
        for char in value:
            card_chars[index][char] += 1

    result = []
    # 주어진 단어를 만들기 위해 각 카드 인덱스에서 사용된 알파벳을 확인
    for word in target:
        # 현재 단어를 확인하기 위해 카드 딕셔너리의 복사본을 생성
        card_chars_copy = copy.deepcopy(card_chars)
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

        valid = True
        for u in line:
            if not u:
                valid = False
        if found and valid:
            result.append(word)

    if not result:
        return ["-1"]

    return result

if __name__ == '__main__':
    print(solution(["ABACDEFG", "NOPQRSTU", "HIJKLKMM"], ["G", "GPMZ", "EFU", "M"]))
    print(solution(["ABACDEFG", "NOPQRSTU", "HIJKLKMM"], ["AAAKKKKKMMMMM", "ABCDKJ"]))