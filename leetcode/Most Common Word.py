from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        ban = set()
        dic = defaultdict(int)

        for b in banned:
            ban.add(b)

        n = len(paragraph)

        arr = []
        for i in range(n):

            if paragraph[i].isalpha():
                arr.append(paragraph[i])
                if i != n - 1:
                    continue
                word = ''.join(arr).lower()
                if word not in ban:
                    dic[word] += 1

            elif len(arr) != 0:
                word = ''.join(arr).lower()
                if word not in ban:
                    dic[word] += 1
                arr = []

        max_count = 0
        max_element = ""
        for k, v in dic.items():
            if v > max_count:
                max_element = k
                max_count = v

        return max_element

