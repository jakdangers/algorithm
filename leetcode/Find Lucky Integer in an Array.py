from collections import defaultdict


class Solution:
    def findLucky(self, arr: List[int]) -> int:

        dic = defaultdict(int)

        for num in arr:
            dic[num] += 1

        result = []

        for i, v in dic.items():
            if i == v:
                result.append(i)

        if len(result) == 0:
            return -1

        result.sort()

        return result[-1]

