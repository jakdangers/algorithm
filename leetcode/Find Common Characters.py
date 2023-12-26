from collections import defaultdict


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        dic = defaultdict(int)

        for c in words[0]:
            dic[c] += 1

        for word in words[1:]:

            temp = defaultdict(int)

            for c in word:
                temp[c] += 1

            keys = list(dic.keys())

            for k in keys:
                if k not in temp:
                    dic[k] = 0
                elif k in temp and temp[k] != dic[k]:
                    if temp[k] < dic[k]:
                        dic[k] = temp[k]

        result = []

        for k, v in dic.items():
            for _ in range(v):
                result.append(k)

        return result

